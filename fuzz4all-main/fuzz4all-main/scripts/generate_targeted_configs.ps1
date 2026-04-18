param(
    [string]$DocumentationDir = "config/documentation",
    [string]$TargetedDir = "config/targeted"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Get-ApiMetadata {
    param(
        [Parameter(Mandatory = $true)]
        [string]$DocBaseName
    )

    $parts = $DocBaseName -split "_"
    if ($parts.Length -lt 2) {
        throw "Unsupported documentation name: $DocBaseName"
    }

    $moduleName = $parts[0]
    $simpleParts = @($parts[1..($parts.Length - 1)])
    $packageName = ($simpleParts[0..($simpleParts.Length - 2)] -join ".")
    $typeName = $simpleParts[-1]
    $qualifiedName = if ([string]::IsNullOrWhiteSpace($packageName)) {
        $typeName
    } else {
        "$packageName.$typeName"
    }

    $leafName = ($typeName -split "\.")[-1]

    return @{
        ModuleName    = $moduleName
        PackageName   = $packageName
        TypeName      = $typeName
        QualifiedName = $qualifiedName
        LeafName      = $leafName
    }
}

function New-TargetedConfigContent {
    param(
        [Parameter(Mandatory = $true)]
        [string]$DocRelativePath,
        [Parameter(Mandatory = $true)]
        [string]$DocBaseName
    )

    $meta = Get-ApiMetadata -DocBaseName $DocBaseName
    $trigger = "/* Please create a very short Java program that uses $($meta.QualifiedName) in diverse and tricky ways. Exercise realistic API calls, edge-case argument combinations, nested types when relevant, and error-prone usage patterns that still try to compile. */"

    @"
# Auto-generated targeted configuration for $($meta.QualifiedName)
# Documentation source: $DocRelativePath

fuzzing:
  output_folder: outputs/targeted/$DocBaseName
  num: 10000
  total_time: 24
  log_level: 3
  otf: true
  resume: true
  evaluate: false
  use_hand_written_prompt: false
  no_input_prompt: false
  prompt_strategy: 2

target:
  language: java
  java_version: 21
  enable_preview: true
  runtime_feedback_mode: normalized
  max_feedback_rules: 5
  max_safe_examples: 2
  prompt_refresh_interval: 5
  prompt_refresh_candidates: 2
  enable_mutation: true
  mutation_budget_per_seed: 2
  mutation_operator_topk: 8
  path_classification_result: outputs/api_classification/java_api_5d_classification.json
  path_documentation: $DocRelativePath
  path_example_code:
  trigger_to_generate_input: "$trigger"
  input_hint: "import $($meta.QualifiedName);"
  path_hand_written_prompt:
  target_string: "$($meta.LeafName)"

llm:
  temperature: 1
  batch_size: 30
  device: cuda
  model_name: Qwen/Qwen2.5-Coder-7B-Instruct
  max_length: 1024
  autoprompt_model: deepseek-chat
  autoprompt_candidates: 3
  autoprompt_temperature: 0.9
  autoprompt_greedy_temperature: 0.2
  autoprompt_max_tokens: 256
  autoprompt_validation_batch_size: 8
  autoprompt_validation_max_length: 512
  runtime_autoprompt_model: deepseek-chat
  runtime_autoprompt_temperature: 0.7
  runtime_autoprompt_max_tokens: 256
  runtime_refresh_validation_batch_size: 4
  runtime_refresh_validation_max_length: 384
"@
}

if (-not (Test-Path $DocumentationDir)) {
    throw "Documentation directory not found: $DocumentationDir"
}

New-Item -ItemType Directory -Force -Path $TargetedDir | Out-Null

$docs = Get-ChildItem -Path $DocumentationDir -Filter *.md -File | Sort-Object Name

foreach ($doc in $docs) {
    $docBaseName = [System.IO.Path]::GetFileNameWithoutExtension($doc.Name)
    $relativeDocPath = "config/documentation/$($doc.Name)"
    $targetFile = Join-Path $TargetedDir "$docBaseName.yaml"
    $content = New-TargetedConfigContent -DocRelativePath $relativeDocPath -DocBaseName $docBaseName
    Set-Content -Path $targetFile -Value $content -Encoding UTF8
}

Write-Host "Generated $($docs.Count) targeted config files in $TargetedDir"

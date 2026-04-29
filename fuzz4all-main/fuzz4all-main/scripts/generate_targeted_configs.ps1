param(
    [string]$DocumentationDir = "config/documentation",
    [string]$TargetedDir = "config/targeted",
    [string]$ClassificationPath = "outputs/api_classification/java_api_5d_classification.json"
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

function Get-ClassificationLookup {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path
    )

    if (-not (Test-Path $Path)) {
        return @{}
    }

    $raw = Get-Content -Path $Path -Raw -Encoding UTF8 | ConvertFrom-Json
    $lookup = @{}
    foreach ($item in $raw) {
        if ($null -ne $item.file) {
            $lookup[$item.file] = $item
        }
    }
    return $lookup
}

function Get-CategoryDefaults {
    param(
        [Parameter(Mandatory = $true)]
        [string]$PrimaryTag,
        [Parameter(Mandatory = $true)]
        [hashtable]$Meta
    )

    $qualifiedName = $Meta.QualifiedName

    $defaults = @{
        MaxSafeExamples                    = 3
        PromptRefreshInterval              = 2
        PromptRefreshCandidates            = 1
        MutationOperatorTopK               = 6
        AutoPromptCandidates               = 1
        AutoPromptValidationBatchSize      = 2
        AutoPromptValidationMaxLength      = 192
        RuntimeRefreshValidationBatchSize  = 2
        RuntimeRefreshValidationMaxLength  = 192
        Trigger                            = "/* Please create a very short Java program that uses $qualifiedName in diverse and tricky ways. Use only standard JDK public APIs. Focus on documented method overloads, edge-case argument combinations, realistic lifecycle or state transitions when relevant, and code that still tries to compile, but avoid fabricated helper classes or undocumented methods. */"
    }

    switch ($PrimaryTag) {
        "SECURITY" {
            $defaults.Trigger = "/* Please create a very short Java program that uses $qualifiedName in diverse and tricky ways. Use only standard JDK security or crypto APIs. Focus on documented algorithms, providers, key or parameter material, and edge-case but type-correct public method combinations, while avoiding fabricated helper methods, guessed providers, or non-JDK security wrappers. */"
        }
        "FILE" {
            $defaults.Trigger = "/* Please create a very short Java program that uses $qualifiedName in diverse and tricky ways. Use only standard JDK file or path APIs. Focus on constructor and path variations, lifecycle or state transitions, permission-style toggles when relevant, and documented public methods, but avoid fabricated helper methods or undocumented filesystem shortcuts. */"
        }
        "CONCURRENT" {
            $defaults.Trigger = "/* Please create a very short Java program that uses $qualifiedName in diverse and tricky ways. Use only standard JDK concurrency APIs. Focus on lifecycle ordering, scheduling or interrupt boundaries, wrapper or helper objects with valid types, and documented public methods, while avoiding fabricated synchronization helpers or illegal control-flow scaffolding. */"
        }
        "REFLECT" {
            $defaults.Trigger = "/* Please create a very short Java program that uses $qualifiedName in diverse and tricky ways. Use only standard JDK reflection APIs and public imports. Focus on member lookup, accessibility changes, receiver or value mismatches, and overload or varargs edge cases, but avoid third-party helpers, illegal declarations, or fabricated APIs. */"
        }
        "CALLBACK" {
            $defaults.MutationOperatorTopK = 5
            $defaults.Trigger = "/* Please create a very short Java program that uses $qualifiedName in diverse and tricky ways. Use only standard JDK listener, event, or callback APIs. Focus on documented add/remove or fire-style overloads, registration order, duplicate or null listener cases when valid, and concrete callback argument types, but avoid fabricated indexed helpers, undocumented listener methods, or third-party event classes. */"
        }
        "TIME" {
            $defaults.Trigger = "/* Please create a very short Java program that uses $qualifiedName in diverse and tricky ways. Use only standard JDK time APIs. Focus on zero, negative, parsed, very large, or arithmetic boundary values, zone or unit conversions when relevant, and documented factory or instance methods, but avoid fabricated temporal helpers or undefined time types. */"
        }
        "NETWORK" {
            $defaults.Trigger = "/* Please create a very short Java program that uses $qualifiedName in diverse and tricky ways. Use only standard JDK networking APIs. Focus on endpoint construction, bind or connect ordering, timeout or state boundaries, and documented public lifecycle methods, but avoid real external dependencies, fabricated helpers, or undocumented networking shortcuts. */"
        }
        "JVM_MGMT" {
            $defaults.MutationOperatorTopK = 5
            $defaults.Trigger = "/* Please create a very short Java program that uses $qualifiedName in diverse and tricky ways. Use only standard JDK management and MXBean APIs. Focus on documented platform MXBean queries, runtime or memory sampling boundaries, valid management object names when required, and public factory methods, but avoid fabricated bean methods, non-JDK wrappers, or guessed management helpers. */"
        }
        "RESOURCE" {
            $defaults.Trigger = "/* Please create a very short Java program that uses $qualifiedName in diverse and tricky ways. Use only standard JDK IO or resource APIs. Focus on lifecycle ordering, constructor size or wrapper boundaries, checked-exception-safe public methods, and stream or reader state transitions such as read, skip, available, mark, or reset when relevant, but avoid fabricated getters or undocumented internals. */"
        }
        "MARK_SUPPORT" {
            $defaults.Trigger = "/* Please create a very short Java program that uses $qualifiedName in diverse and tricky ways. Use only standard JDK APIs. Focus on documented mark or reset limits, lifecycle ordering, and valid stream or reader state transitions, but avoid fabricated state getters or undocumented internals. */"
        }
        "UTILITY" {
            $defaults.Trigger = "/* Please create a very short Java program that uses $qualifiedName in diverse and tricky ways. Use only standard JDK parse, format, and value-conversion APIs. Focus on normalization, parsing, formatting, value boundary cases, and documented public helpers, but avoid fabricated helper methods, external libraries, or undocumented shortcuts. */"
        }
    }

    return $defaults
}

function New-TargetedConfigContent {
    param(
        [Parameter(Mandatory = $true)]
        [string]$DocRelativePath,
        [Parameter(Mandatory = $true)]
        [string]$DocBaseName,
        [Parameter(Mandatory = $true)]
        [hashtable]$ClassificationLookup
    )

    $meta = Get-ApiMetadata -DocBaseName $DocBaseName
    $primaryTag = ""
    if ($ClassificationLookup.ContainsKey($DocRelativePath)) {
        $primaryTag = [string]$ClassificationLookup[$DocRelativePath].primary_tag
    }
    $defaults = Get-CategoryDefaults -PrimaryTag $primaryTag -Meta $meta

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
  max_safe_examples: $($defaults.MaxSafeExamples)
  prompt_refresh_interval: $($defaults.PromptRefreshInterval)
  prompt_refresh_candidates: $($defaults.PromptRefreshCandidates)
  enable_mutation: true
  mutation_budget_per_seed: 2
  mutation_operator_topk: $($defaults.MutationOperatorTopK)
  path_classification_result: outputs/api_classification/java_api_5d_classification.json
  path_documentation: $DocRelativePath
  path_example_code:
  trigger_to_generate_input: "$($defaults.Trigger)"
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
  autoprompt_candidates: $($defaults.AutoPromptCandidates)
  autoprompt_temperature: 0.9
  autoprompt_greedy_temperature: 0.2
  autoprompt_max_tokens: 256
  autoprompt_validation_batch_size: $($defaults.AutoPromptValidationBatchSize)
  autoprompt_validation_max_length: $($defaults.AutoPromptValidationMaxLength)
  runtime_autoprompt_model: deepseek-chat
  runtime_autoprompt_temperature: 0.7
  runtime_autoprompt_max_tokens: 256
  runtime_refresh_validation_batch_size: $($defaults.RuntimeRefreshValidationBatchSize)
  runtime_refresh_validation_max_length: $($defaults.RuntimeRefreshValidationMaxLength)
"@
}

if (-not (Test-Path $DocumentationDir)) {
    throw "Documentation directory not found: $DocumentationDir"
}

New-Item -ItemType Directory -Force -Path $TargetedDir | Out-Null

$classificationLookup = Get-ClassificationLookup -Path $ClassificationPath
$docs = Get-ChildItem -Path $DocumentationDir -Filter *.md -File | Sort-Object Name

foreach ($doc in $docs) {
    $docBaseName = [System.IO.Path]::GetFileNameWithoutExtension($doc.Name)
    $relativeDocPath = "config/documentation/$($doc.Name)"
    $targetFile = Join-Path $TargetedDir "$docBaseName.yaml"
    $content = New-TargetedConfigContent -DocRelativePath $relativeDocPath -DocBaseName $docBaseName -ClassificationLookup $classificationLookup
    Set-Content -Path $targetFile -Value $content -Encoding UTF8
}

Write-Host "Generated $($docs.Count) targeted config files in $TargetedDir"

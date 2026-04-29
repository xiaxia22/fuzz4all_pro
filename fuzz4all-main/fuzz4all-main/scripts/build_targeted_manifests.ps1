param(
    [string]$RootDir = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$classificationFile = Join-Path $RootDir "outputs\api_classification\java_api_5d_classification.json"
$targetedDir = Join-Path $RootDir "config\targeted"
$outDir = Join-Path $RootDir "config\targeted_groups"

if (-not (Test-Path $classificationFile)) {
    throw "Missing classification file: $classificationFile"
}

$classification = Get-Content $classificationFile -Raw | ConvertFrom-Json
$groups = @{
    primary_tag      = @{}
    mutation_profile = @{}
    module           = @{}
    package          = @{}
}

foreach ($item in $classification) {
    $configPath = $item.file.Replace("config/documentation/", "config/targeted/").Replace(".md", ".yaml")
    $configAbs = Join-Path $RootDir $configPath.Replace("/", "\")
    if (-not (Test-Path $configAbs)) {
        continue
    }

    $stem = [System.IO.Path]::GetFileNameWithoutExtension($configPath)
    $parts = $stem -split "_"
    $module = $parts[0]
    $package = if ($parts.Length -le 2) { "root" } else { ($parts[1..($parts.Length - 2)] -join ".") }

    $dimensions = @(
        @{ Name = "primary_tag"; Key = [string]$item.primary_tag },
        @{ Name = "mutation_profile"; Key = [string]$item.mutation_profile },
        @{ Name = "module"; Key = [string]$module },
        @{ Name = "package"; Key = [string]$package }
    )

    foreach ($dimension in $dimensions) {
        if (-not $groups[$dimension.Name].ContainsKey($dimension.Key)) {
            $groups[$dimension.Name][$dimension.Key] = New-Object System.Collections.Generic.List[string]
        }
        $groups[$dimension.Name][$dimension.Key].Add($configPath)
    }
}

New-Item -ItemType Directory -Force -Path $outDir | Out-Null

$summary = New-Object System.Collections.Generic.List[string]
$summary.Add('# Targeted Group Summary')
$summary.Add('')
$summary.Add('- Classification source: `outputs/api_classification/java_api_5d_classification.json`')
$summary.Add('- Targeted config root: `config/targeted`')
$summary.Add('')

foreach ($dimensionName in @("primary_tag", "mutation_profile", "module", "package")) {
    $dimensionDir = Join-Path $outDir $dimensionName
    New-Item -ItemType Directory -Force -Path $dimensionDir | Out-Null
    $summary.Add("## $dimensionName")
    $summary.Add('')

    foreach ($groupName in ($groups[$dimensionName].Keys | Sort-Object)) {
        $items = @($groups[$dimensionName][$groupName] | Sort-Object)
        $targetFile = Join-Path $dimensionDir "$groupName.txt"
        Set-Content -Path $targetFile -Value ($items -join [Environment]::NewLine) -Encoding utf8
        $summary.Add("- $groupName`: $($items.Count)")
    }

    $summary.Add('')
}

Set-Content -Path (Join-Path $outDir "README.md") -Value ($summary -join [Environment]::NewLine) -Encoding utf8
Write-Host "Generated targeted group manifests in $outDir"

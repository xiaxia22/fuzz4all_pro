$ErrorActionPreference = "Stop"

param(
    [string]$ModelName = "ollama/qwen2.5:7b",
    [string]$OutputRoot = "outputs/targeted200",
    [switch]$UseAutopromptJvmmgmt
)

$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

$pythonCmd = "python"
$tempConfigDir = Join-Path $repoRoot "config\targeted_200_temp"
New-Item -ItemType Directory -Force -Path $tempConfigDir | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $repoRoot $OutputRoot) | Out-Null

$targets = @(
    "java.base_java_io_BufferedInputStream.yaml",
    "java.base_java_io_File.yaml",
    "java.base_java_lang_Thread.yaml",
    "java.base_java_lang_reflect_Method.yaml",
    "java.base_java_net_Socket.yaml",
    "java.base_java_net_URI.yaml",
    "java.base_java_time_Duration.yaml",
    "java.base_javax_crypto_Cipher.yaml",
    "java.desktop_java_beans_PropertyChangeSupport.yaml"
)

if ($UseAutopromptJvmmgmt) {
    $targets += "java.management_java_lang_management_ManagementFactory_autoprompt.yaml"
} else {
    $targets += "java.management_java_lang_management_ManagementFactory.yaml"
}

function Update-YamlLine {
    param(
        [string[]]$Lines,
        [string]$Pattern,
        [string]$Replacement
    )
    $updated = $false
    for ($i = 0; $i -lt $Lines.Length; $i++) {
        if ($Lines[$i] -match $Pattern) {
            $Lines[$i] = $Replacement
            $updated = $true
        }
    }
    if (-not $updated) {
        $Lines += $Replacement
    }
    return ,$Lines
}

foreach ($target in $targets) {
    $sourcePath = Join-Path $repoRoot ("config\targeted\" + $target)
    $targetBase = [System.IO.Path]::GetFileNameWithoutExtension($target)
    $destPath = Join-Path $tempConfigDir $target
    $runOutput = Join-Path $OutputRoot $targetBase

    $lines = Get-Content $sourcePath

    $lines = Update-YamlLine $lines '^\s*num:\s*\d+' '  num: 200'
    $lines = Update-YamlLine $lines '^\s*resume:\s*(true|false)' '  resume: false'
    $lines = Update-YamlLine $lines '^\s*output_folder:\s*.+$' ("  output_folder: " + $runOutput)

    # Make prompt selection a little more stable for final runs without changing the whole system logic.
    $lines = Update-YamlLine $lines '^\s*temperature:\s*[\d\.]+' '  temperature: 0.9'
    $lines = Update-YamlLine $lines '^\s*autoprompt_candidates:\s*\d+' '  autoprompt_candidates: 4'
    $lines = Update-YamlLine $lines '^\s*autoprompt_temperature:\s*[\d\.]+' '  autoprompt_temperature: 0.7'
    $lines = Update-YamlLine $lines '^\s*autoprompt_validation_batch_size:\s*\d+' '  autoprompt_validation_batch_size: 10'
    $lines = Update-YamlLine $lines '^\s*runtime_autoprompt_temperature:\s*[\d\.]+' '  runtime_autoprompt_temperature: 0.6'
    $lines = Update-YamlLine $lines '^\s*runtime_refresh_validation_batch_size:\s*\d+' '  runtime_refresh_validation_batch_size: 5'

    Set-Content -Path $destPath -Value $lines -Encoding UTF8

    Write-Host "=== Running $targetBase ===" -ForegroundColor Cyan
    Write-Host "Config: $destPath" -ForegroundColor DarkGray
    Write-Host "Output: $runOutput" -ForegroundColor DarkGray

    & $pythonCmd Fuzz4All/fuzz.py --config $destPath main_with_config --folder $runOutput --model_name $ModelName --target javac

    if ($LASTEXITCODE -ne 0) {
        throw "Run failed for $targetBase with exit code $LASTEXITCODE"
    }
}

Write-Host "All 10 targeted runs completed." -ForegroundColor Green

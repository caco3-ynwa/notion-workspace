param([string]$PythonExe = "python")
$ErrorActionPreference = "Stop"
$projectDir = Split-Path -Parent $PSScriptRoot
Push-Location $projectDir
try {
    & $PythonExe -m PyInstaller --noconfirm --onefile --name notion-sync `
        --paths "$projectDir/python/src" `
        --add-data "$projectDir/python/src/notion_workspace/dota/dict/heroes.csv;notion_workspace/dota/dict" `
        --collect-data tzdata `
        --distpath "$projectDir/dist/python" `
        --workpath "$projectDir/build/python/work" `
        --specpath "$projectDir/build/python" `
        "$projectDir/python/src/notion_workspace/main.py"
    if ($LASTEXITCODE -ne 0) { throw "PyInstaller failed: $LASTEXITCODE" }
} finally {
    Pop-Location
}

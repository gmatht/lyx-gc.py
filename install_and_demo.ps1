# Install LyX-GC on Windows from the GitHub release.
#
# 1. Searches for LyX; installs via winget/choco if not found
# 2. Uses Python from LyX bundle (Windows often lacks system Python)
# 3. Downloads release, runs check_deps.py --all, launches LyX with sample file
#
# Usage: .\install_and_demo.ps1
# Requires: PowerShell 5.1+, internet access

$ErrorActionPreference = "Stop"
$REPO = "https://github.com/gmatht/lyx-gc.py"
$RELEASE_TAG = "v0.1.0dev2"

function Find-LyX {
    $bases = @(
        $env:ProgramFiles,
        ${env:ProgramFiles(x86)},
        "C:\Program Files",
        "C:\Program Files (x86)"
    ) | Where-Object { $_ }
    $versions = @("LyX 2.4", "LyX 2.3", "LyX 2.2", "LyX 2.1")
    foreach ($base in $bases) {
        foreach ($ver in $versions) {
            $exe = Join-Path $base "$ver\bin\lyx.exe"
            if (Test-Path $exe -PathType Leaf) {
                return $exe
            }
        }
    }
    return $null
}

function Find-PythonForLyX {
    param([string]$LyXPath)
    # LyX may bundle Python (e.g. Resources\Python, Python39, etc.)
    $lyxDir = Split-Path (Split-Path $LyXPath -Parent) -Parent
    $candidates = @(
        (Join-Path $lyxDir "Resources\Python\python.exe"),
        (Join-Path $lyxDir "Python\python.exe"),
        (Join-Path $lyxDir "Python39\python.exe"),
        (Join-Path $lyxDir "Python311\python.exe"),
        (Join-Path $lyxDir "Python310\python.exe")
    )
    foreach ($c in $candidates) {
        if (Test-Path $c -PathType Leaf) { return @{ Exe = $c; Args = @() } }
    }
    # Fallback: py launcher (Windows may not have python by default)
    $py = Get-Command "py" -ErrorAction SilentlyContinue
    if ($py) { return @{ Exe = "py"; Args = @("-3") } }
    foreach ($name in @("python3", "python")) {
        $p = Get-Command $name -ErrorAction SilentlyContinue
        if ($p) { return @{ Exe = $p.Source; Args = @() } }
    }
    return $null
}

function Install-LyX {
    Write-Host "Attempting to install LyX..."
    if (Get-Command winget -ErrorAction SilentlyContinue) {
        try {
            winget install LyX.LyX --accept-package-agreements
            return $true
        } catch {
            Write-Host "winget install failed: $_"
        }
    }
    if (Get-Command choco -ErrorAction SilentlyContinue) {
        try {
            choco install lyx -y
            return $true
        } catch {
            Write-Host "choco install failed: $_"
        }
    }
    Write-Host "LyX not found. Install from https://www.lyx.org/"
    return $false
}

function Main {
    Write-Host "LyX-GC Windows install and demo"
    Write-Host ""

    # 1. Find or install LyX
    $lyxExe = Find-LyX
    if (-not $lyxExe) {
        if (-not (Install-LyX)) { exit 1 }
        $lyxExe = Find-LyX
        if (-not $lyxExe) {
            Write-Host "LyX still not found. Restart the shell and retry."
            exit 1
        }
    }
    Write-Host "LyX: $lyxExe"

    # 2. Find Python (prefer LyX-bundled; Windows may not have system Python)
    $pyInfo = Find-PythonForLyX -LyXPath $lyxExe
    if (-not $pyInfo) {
        Write-Host "Python not found. lyx-gc requires Python 3.9+."
        Write-Host "Install from https://www.python.org/ or use LyX which may bundle Python."
        exit 1
    }
    Write-Host "Python: $($pyInfo.Exe) $($pyInfo.Args -join ' ')"

    # 3. Download release
    $url = "$REPO/archive/refs/tags/$RELEASE_TAG.zip"
    $extractDir = Join-Path $env:TEMP "lyx-gc-install"
    if (Test-Path $extractDir) { Remove-Item -Recurse -Force $extractDir }
    New-Item -ItemType Directory -Path $extractDir | Out-Null
    $zipPath = Join-Path $extractDir "release.zip"

    Write-Host "Downloading $url ..."
    try {
        Invoke-WebRequest -Uri $url -OutFile $zipPath -UseBasicParsing
    } catch {
        Write-Host "Download failed: $_"
        exit 1
    }

    Write-Host "Extracting..."
    Expand-Archive -Path $zipPath -DestinationPath $extractDir -Force

    $extracted = Get-ChildItem $extractDir -Directory | Select-Object -First 1
    $pyDir = Join-Path $extracted.FullName "py"
    if (-not (Test-Path (Join-Path $pyDir "chktex.py"))) {
        $pyDir = $extracted.FullName
    }
    if (-not (Test-Path (Join-Path $pyDir "chktex.py"))) {
        Write-Host "chktex.py not found in extracted files"
        exit 1
    }

    # 4. Run check_deps --all
    Write-Host ""
    Write-Host "Running check_deps.py --all ..."
    & $pyInfo.Exe @pyInfo.Args (Join-Path $pyDir "check_deps.py") --all
    if ($LASTEXITCODE -ne 0) {
        Write-Host "check_deps.py had issues (some deps may be missing)"
    }

    # 5. Launch LyX with sample
    $sample = Join-Path $pyDir "sample_errors.lyx"
    $runLyx = Join-Path $pyDir "run_lyx.py"
    if (-not (Test-Path $sample)) {
        Write-Host "sample_errors.lyx not found"
        exit 1
    }

    Write-Host ""
    Write-Host "Launching LyX with sample document..."
    Write-Host "Use Tools > Check Text to run lyx-gc on the document."
    Write-Host ""

    Push-Location $pyDir
    try {
        & $pyInfo.Exe @pyInfo.Args $runLyx $sample
    } finally {
        Pop-Location
    }
}

Main

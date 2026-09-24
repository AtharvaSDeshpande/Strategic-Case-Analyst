<#
.SYNOPSIS
    Optional installer for this playbook's diagram-rendering tooling.

.DESCRIPTION
    Nothing in this repository requires these tools: every skill file works as plain prompt text
    with no tooling at all. This script exists only so that, if you *do* want the assistant to be
    able to actually render the framework exhibits (crosses, two-by-two grids, bubble matrices,
    value chains, node-link diagrams) instead of just describing them, you can install everything
    needed with one command instead of hunting it down yourself.

    Nothing here runs unless you run this script. Nothing installs silently.

    Installs, if missing:
      - Python packages: matplotlib (fixed-layout exhibits), graphviz (Python wrapper only)
      - The Graphviz system binary (`dot`), via winget or choco, for node-link diagrams
      - Optionally, Understand-Anything (an external, separately maintained project) for
        knowledge-graph rendering, only if you pass -IncludeKnowledgeGraphTool

.PARAMETER CheckOnly
    Report what is and isn't installed, and do nothing else.

.PARAMETER IncludeKnowledgeGraphTool
    Also clone https://github.com/Egonex-AI/Understand-Anything into tools/understand-anything.
    Off by default: it's a separate project with its own license and setup, and the workflow has a
    hand-authored fallback if you skip it.

.EXAMPLE
    .\install-optional-deps.ps1 -CheckOnly
    .\install-optional-deps.ps1
    .\install-optional-deps.ps1 -IncludeKnowledgeGraphTool
#>

param(
    [switch]$CheckOnly,
    [switch]$IncludeKnowledgeGraphTool
)

$ErrorActionPreference = "Continue"
$RepoRoot = Split-Path -Parent $PSScriptRoot

function Test-Command($name) {
    return [bool](Get-Command $name -ErrorAction SilentlyContinue)
}

function Test-PythonModule($module) {
    if (-not (Test-Command "python")) { return $false }
    python -c "import $module" 2>$null
    return $LASTEXITCODE -eq 0
}

$results = [ordered]@{
    "Python"                  = Test-Command "python"
    "matplotlib (pip package)" = Test-PythonModule "matplotlib"
    "graphviz (pip wrapper)"   = Test-PythonModule "graphviz"
    "dot (Graphviz binary)"    = Test-Command "dot"
    "git"                      = Test-Command "git"
}

Write-Host ""
Write-Host "Optional diagram tooling  -  current status" -ForegroundColor Cyan
Write-Host "-------------------------------------------"
foreach ($k in $results.Keys) {
    $status = if ($results[$k]) { "OK" } else { "missing" }
    $color = if ($results[$k]) { "Green" } else { "Yellow" }
    Write-Host ("{0,-28} {1}" -f $k, $status) -ForegroundColor $color
}
Write-Host ""

if ($CheckOnly) {
    Write-Host "Check-only run  -  nothing was installed."
    exit 0
}

$summary = @()

# --- Python packages -------------------------------------------------------
if (-not $results["Python"]) {
    Write-Host "Python was not found on PATH. Install Python 3 first (python.org), then re-run this" -ForegroundColor Yellow
    Write-Host "script to install matplotlib and the graphviz wrapper." -ForegroundColor Yellow
    $summary += "SKIPPED: matplotlib, graphviz (pip wrapper)  -  Python not found"
}
else {
    foreach ($pkg in @("matplotlib", "graphviz")) {
        if (Test-PythonModule $pkg) {
            $summary += "OK (already installed): $pkg"
        }
        else {
            Write-Host "Installing Python package: $pkg ..." -ForegroundColor Cyan
            python -m pip install --quiet $pkg
            if (Test-PythonModule $pkg) {
                $summary += "INSTALLED: $pkg"
            }
            else {
                $summary += "FAILED: $pkg  -  run 'python -m pip install $pkg' manually and check the error"
            }
        }
    }
}

# --- Graphviz binary ---------------------------------------------------------
if (Test-Command "dot") {
    $summary += "OK (already installed): dot (Graphviz binary)"
}
elseif (Test-Command "winget") {
    Write-Host "Installing Graphviz via winget ..." -ForegroundColor Cyan
    winget install --id Graphviz.Graphviz -e --accept-source-agreements --accept-package-agreements
    if (Test-Command "dot") {
        $summary += "INSTALLED: dot (Graphviz binary), via winget"
    }
    else {
        $summary += "FAILED or needs a new terminal: dot (Graphviz binary)  -  open a new shell and re-run -CheckOnly to confirm"
    }
}
elseif (Test-Command "choco") {
    Write-Host "Installing Graphviz via choco ..." -ForegroundColor Cyan
    choco install graphviz -y
    if (Test-Command "dot") {
        $summary += "INSTALLED: dot (Graphviz binary), via choco"
    }
    else {
        $summary += "FAILED or needs a new terminal: dot (Graphviz binary)  -  open a new shell and re-run -CheckOnly to confirm"
    }
}
else {
    $summary += "SKIPPED: dot (Graphviz binary)  -  no winget or choco found; install manually from https://graphviz.org/download/"
}

# --- Optional: Understand-Anything -------------------------------------------
if ($IncludeKnowledgeGraphTool) {
    if (-not (Test-Command "git")) {
        $summary += "SKIPPED: Understand-Anything  -  git not found; install git first"
    }
    else {
        $target = Join-Path $RepoRoot "tools\understand-anything"
        if (Test-Path $target) {
            $summary += "OK (already present): Understand-Anything at tools\understand-anything"
        }
        else {
            Write-Host "Cloning Understand-Anything into tools\understand-anything ..." -ForegroundColor Cyan
            git clone --quiet https://github.com/Egonex-AI/Understand-Anything.git $target
            if (Test-Path $target) {
                $summary += "CLONED: Understand-Anything into tools\understand-anything  -  follow that project's own setup instructions inside it before relying on it"
            }
            else {
                $summary += "FAILED: Understand-Anything clone  -  check network access and try 'git clone https://github.com/Egonex-AI/Understand-Anything.git' manually"
            }
        }
    }
}
else {
    $summary += "SKIPPED (by default): Understand-Anything  -  re-run with -IncludeKnowledgeGraphTool if you want it; the workflow has a hand-authored fallback without it"
}

Write-Host ""
Write-Host "Summary" -ForegroundColor Cyan
Write-Host "-------"
$summary | ForEach-Object { Write-Host $_ }
Write-Host ""
Write-Host "Re-run with -CheckOnly at any time to confirm what's actually installed."

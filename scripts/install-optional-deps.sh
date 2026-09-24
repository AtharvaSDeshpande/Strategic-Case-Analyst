#!/usr/bin/env bash
# Optional installer for this playbook's diagram-rendering tooling.
#
# Nothing in this repository requires these tools: every skill file works as plain prompt text
# with no tooling at all. This script exists only so that, if you *do* want the assistant to be
# able to actually render the framework exhibits (crosses, two-by-two grids, bubble matrices,
# value chains, node-link diagrams) instead of just describing them, you can install everything
# needed with one command instead of hunting it down yourself.
#
# Nothing here runs unless you run this script. Nothing installs silently.
#
# Installs, if missing:
#   - Python packages: matplotlib (fixed-layout exhibits), graphviz (Python wrapper only)
#   - The Graphviz system binary (`dot`), via apt/dnf/brew, for node-link diagrams
#   - Optionally, Understand-Anything (an external, separately maintained project) for
#     knowledge-graph rendering, only if you pass --with-knowledge-graph-tool
#
# Usage:
#   ./install-optional-deps.sh --check-only
#   ./install-optional-deps.sh
#   ./install-optional-deps.sh --with-knowledge-graph-tool

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

CHECK_ONLY=0
WITH_KG=0
for arg in "$@"; do
    case "$arg" in
        --check-only) CHECK_ONLY=1 ;;
        --with-knowledge-graph-tool) WITH_KG=1 ;;
        *) echo "Unknown argument: $arg" >&2; exit 1 ;;
    esac
done

have() { command -v "$1" >/dev/null 2>&1; }
py_has() { have python3 && python3 -c "import $1" >/dev/null 2>&1; }

echo ""
echo "Optional diagram tooling — current status"
echo "-------------------------------------------"
printf "%-28s %s\n" "python3"                    "$(have python3 && echo OK || echo missing)"
printf "%-28s %s\n" "matplotlib (pip package)"    "$(py_has matplotlib && echo OK || echo missing)"
printf "%-28s %s\n" "graphviz (pip wrapper)"      "$(py_has graphviz && echo OK || echo missing)"
printf "%-28s %s\n" "dot (Graphviz binary)"       "$(have dot && echo OK || echo missing)"
printf "%-28s %s\n" "git"                         "$(have git && echo OK || echo missing)"
echo ""

if [ "$CHECK_ONLY" -eq 1 ]; then
    echo "Check-only run — nothing was installed."
    exit 0
fi

summary=()

# --- Python packages ---------------------------------------------------------
if ! have python3; then
    echo "python3 was not found on PATH. Install Python 3 first, then re-run this script to install"
    echo "matplotlib and the graphviz wrapper."
    summary+=("SKIPPED: matplotlib, graphviz (pip wrapper) — python3 not found")
else
    for pkg in matplotlib graphviz; do
        if py_has "$pkg"; then
            summary+=("OK (already installed): $pkg")
        else
            echo "Installing Python package: $pkg ..."
            python3 -m pip install --quiet "$pkg"
            if py_has "$pkg"; then
                summary+=("INSTALLED: $pkg")
            else
                summary+=("FAILED: $pkg — run 'python3 -m pip install $pkg' manually and check the error")
            fi
        fi
    done
fi

# --- Graphviz binary -----------------------------------------------------------
if have dot; then
    summary+=("OK (already installed): dot (Graphviz binary)")
elif have brew; then
    echo "Installing Graphviz via brew ..."
    brew install graphviz
    if have dot; then summary+=("INSTALLED: dot (Graphviz binary), via brew"); else summary+=("FAILED: dot (Graphviz binary) via brew — check the error above"); fi
elif have apt-get; then
    echo "Installing Graphviz via apt-get (may prompt for sudo password) ..."
    sudo apt-get update -qq && sudo apt-get install -y graphviz
    if have dot; then summary+=("INSTALLED: dot (Graphviz binary), via apt-get"); else summary+=("FAILED: dot (Graphviz binary) via apt-get — check the error above"); fi
elif have dnf; then
    echo "Installing Graphviz via dnf (may prompt for sudo password) ..."
    sudo dnf install -y graphviz
    if have dot; then summary+=("INSTALLED: dot (Graphviz binary), via dnf"); else summary+=("FAILED: dot (Graphviz binary) via dnf — check the error above"); fi
else
    summary+=("SKIPPED: dot (Graphviz binary) — no brew/apt-get/dnf found; install manually from https://graphviz.org/download/")
fi

# --- Optional: Understand-Anything ----------------------------------------------
if [ "$WITH_KG" -eq 1 ]; then
    if ! have git; then
        summary+=("SKIPPED: Understand-Anything — git not found; install git first")
    else
        target="$REPO_ROOT/tools/understand-anything"
        if [ -d "$target" ]; then
            summary+=("OK (already present): Understand-Anything at tools/understand-anything")
        else
            echo "Cloning Understand-Anything into tools/understand-anything ..."
            git clone --quiet https://github.com/Egonex-AI/Understand-Anything.git "$target"
            if [ -d "$target" ]; then
                summary+=("CLONED: Understand-Anything into tools/understand-anything — follow that project's own setup instructions inside it before relying on it")
            else
                summary+=("FAILED: Understand-Anything clone — check network access and try 'git clone https://github.com/Egonex-AI/Understand-Anything.git' manually")
            fi
        fi
    fi
else
    summary+=("SKIPPED (by default): Understand-Anything — re-run with --with-knowledge-graph-tool if you want it; the workflow has a hand-authored fallback without it")
fi

echo ""
echo "Summary"
echo "-------"
printf "%s\n" "${summary[@]}"
echo ""
echo "Re-run with --check-only at any time to confirm what's actually installed."

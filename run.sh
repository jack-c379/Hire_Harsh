#!/bin/bash
# Run script for Hire_Harsh - automatically activates virtual environment

cd "$(dirname "$0")"

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}' | cut -d. -f1,2)
if [ "$(printf '%s\n' "3.14" "$python_version" | sort -V | head -n1)" = "3.14" ] && [ "$python_version" = "3.14" ]; then
    echo "⚠️  WARNING: Python 3.14 has compatibility issues with ChromaDB."
    echo "   See PYTHON314_FIX.md for solutions."
    echo "   Continuing anyway..."
fi

source .venv/bin/activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000


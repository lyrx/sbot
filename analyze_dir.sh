#!/bin/bash

if [ "$#" -lt 2 ] || [ "$#" -gt 3 ]; then
    echo "Usage: ./run_analyzer.sh <base_path> <key> [githubDir]"
    exit 1
fi

python3 src/analyzedir.py "$1" "$2" "${3:-}"


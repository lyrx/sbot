#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: ./run_analyzer.sh <base_path> <key>"
    exit 1
fi

python3 src/analyzedir.py "$1" "$2"

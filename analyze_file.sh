#!/bin/bash

# Check if both file path and key arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: ./script_name.sh <file_path> <key>"
    exit 1
fi

# Execute the Python script with the provided file path and key
python3 src/analyzefile.py "$1" "$2"

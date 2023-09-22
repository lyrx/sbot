#!/bin/bash

# Check if the file path argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: ./script_name.sh <file_path>"
    exit 1
fi

# Execute the Python script with the provided file path
python3 src/analyzefile.py "$1"

import sys
from solidity_analyzer import analyze_solidity_file
from bloodhounds import check_structures

if len(sys.argv) < 3:
    print("Usage: python analyze_solidity_file.py <file_path> <key>")
    sys.exit(1)

file_path = sys.argv[1]
key = sys.argv[2]

if key not in check_structures:
    print(f"Key '{key}' not found in check_structures.")
    sys.exit(1)

results = analyze_solidity_file(file_path, check_structures[key])
for r in results:
    print(r)

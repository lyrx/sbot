import sys
from solidity_analyzer import analyze_solidity_dir
from bloodhounds import check_structures

def display_analysis(results):
    """
    Display the analysis results for each file.

    Parameters:
    - results (dict): A dictionary containing file paths as keys and their corresponding analysis as values.
    """
    for file_path, analysis in results.items():
        # Only process and print results if the analysis for the file has content
        if len(analysis) > 0:
            print(f"File: {file_path}")
            for i in range(len(analysis)):
                cn = analysis[i]["check_name"]
                msg = analysis[i]["message"]
                line = analysis[i]["line"]
                print(f"{cn}: {msg} (Line {line})")

            print("-" * 50)  # Separator line for clarity

if len(sys.argv) < 3:
    print("Usage: python analyzedir.py <base_path> <key>")
    sys.exit(1)

base_path = sys.argv[1]
key = sys.argv[2]

if key not in check_structures:
    print(f"Key '{key}' not found in check_structures.")
    sys.exit(1)

results = analyze_solidity_dir(base_path, check_structures[key])
display_analysis(results)

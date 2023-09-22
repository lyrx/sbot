from solidity_analyzer import analyze_solidity_dir
from bloodhounds import check_structures

# Test
base_path = "/Users/alex/git/Web3Academy/hats-audit/contracts"
results = analyze_solidity_dir(base_path, check_structures)
for file_path, analysis in results.items():
    print(f"File: {file_path}")
    for i in range(len(analysis)):
        cn = analysis[i]["check_name"]
        msg = analysis[i]["message"]
        line = analysis[i]["line"]
        print(f"{cn}: {msg} (Line {line})")

    print("-" * 50)  # Separator line for clarity

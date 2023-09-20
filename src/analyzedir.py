from solidity_analyzer import analyze_solidity_dir

from solidity_checks import (
    check_outdated_versions,
    check_pragma_experimental,
    check_send_transfer,
    check_low_level_call,
    check_tx_origin,
    check_visibility_specifiers
)



check_structures = [
    {"name": "Outdated Versions", "func": check_outdated_versions},
    {"name": "Pragma Experimental", "func": check_pragma_experimental},
    {"name": "Send/Transfer", "func": check_send_transfer},
    {"name": "Low-Level Call", "func": check_low_level_call},
    {"name": "Tx.Origin", "func": check_tx_origin},
    {"name": "Visibility Specifiers", "func": check_visibility_specifiers}
]


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

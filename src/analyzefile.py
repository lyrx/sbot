from solidity_checks import (
    check_outdated_versions,
    check_pragma_experimental,
    check_send_transfer,
    check_low_level_call,
    check_tx_origin,
    check_visibility_specifiers
)
from solidity_analyzer import analyze_solidity_file  # Import the externalized function


check_structures = [
    {"name": "Outdated Versions", "func": check_outdated_versions},
    {"name": "Pragma Experimental", "func": check_pragma_experimental},
    {"name": "Send/Transfer", "func": check_send_transfer},
    {"name": "Low-Level Call", "func": check_low_level_call},
    {"name": "Tx.Origin", "func": check_tx_origin},
    {"name": "Visibility Specifiers", "func": check_visibility_specifiers}
]

# Test
file_path = "/Users/alex/git/Web3Academy/hats-audit/contracts/CvgControlTower.sol"
results = analyze_solidity_file(file_path, check_structures)
for r in results:
    print(r)

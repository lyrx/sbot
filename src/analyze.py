from solidity_checks import (
    check_outdated_versions,
    check_pragma_experimental,
    check_send_transfer,
    check_low_level_call,
    check_tx_origin,
    check_visibility_specifiers
)
from solidity_analyzer import analyze_solidity_file  # Import the externalized function

# Define the list of checks to use
checks = [
    check_outdated_versions,
    check_pragma_experimental,
    check_send_transfer,
    check_low_level_call,
    check_tx_origin,
    check_visibility_specifiers
]

# Test
# file_path = "sample.sol"
# results = analyze_solidity_file(file_path, checks)
# for r in results:
#     print(r)

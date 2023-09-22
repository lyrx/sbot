from solidity_analyzer import analyze_solidity_file  # Import the externalized function
from bloodhounds import check_structures

# Test
file_path = "/Users/alex/git/Web3Academy/hats-audit/contracts/CvgControlTower.sol"
results = analyze_solidity_file(file_path, check_structures)
for r in results:
    print(r)

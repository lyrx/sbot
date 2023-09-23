import os
from fileutils import findpaths

def analyze_solidity_file(file_path, check_structures):
    with open(file_path, 'r') as f:
        code = f.read()

    findings = []

    # Execute each check and collect findings
    for check_structure in check_structures:
        check_name = check_structure['name']
        check_func = check_structure['func']
        check_findings = check_func(code)

        for finding in check_findings:
            findings.append({
                "file_path": file_path,
                "check_name": check_name,
                "line": finding["line"],
                "message": finding["message"]
            })



    return findings

# Example usage:
# Assuming you have some check functions defined, e.g., check1, check2
# check_structures = [
#     {"name": "Check 1", "func": check1},
#     {"name": "Check 2", "func": check2}
# ]
# findings = analyze_solidity_file('/path/to/solidity/file.sol', check_structures)
# print(findings)

def analyze_solidity_dir(base_dir, check_structures):
    """
    Analyzes all Solidity files in a given base directory based on the provided checks.

    Parameters:
    - base_dir (str): The base directory to search for Solidity files.
    - check_structures (list): A list of check structures to perform on each file.

    Returns:
    - all_results (dict): A dictionary containing the results of the checks for each file.
    """

    paths = findpaths(base_dir, '.sol')
    all_results = {}

    for path in paths:
        all_results[path] = analyze_solidity_file(path, check_structures)

    return all_results

# Example usage:
# Assuming you have some check functions defined, e.g., check1, check2
# check_structures = [
#     {"name": "Check 1", "func": check1},
#     {"name": "Check 2", "func": check2}
# ]
# results = analyze_solidity_dir('/path/to/base/directory', check_structures)
# print(results)

import os

from src.fileutils import findpaths



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
                "message": finding
            })

    # If there are no findings, add a "no findings" entry
    if not findings:
        findings.append({
            "file_path": file_path,
            "check_name": "General",
            "message": f"{os.path.basename(file_path)}: no findings"
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




def analyze_solidity_dir(base_dir, checks):
    """
    Analyzes all Solidity files in a given base directory based on the provided checks.

    Parameters:
    - base_dir (str): The base directory to search for Solidity files.
    - checks (list): A list of checks to perform on each file.

    Returns:
    - all_results (dict): A dictionary containing the results of the checks for each file.
    """

    paths = findpaths(base_dir, '.sol')
    all_results = {}

    for path in paths:
        all_results[path] = analyze_solidity_file(path, checks)

    return all_results

# Example usage:
# checks = ["Check1", "Check2"]
# results = analyze_solidity_dir('/path/to/base/directory', checks)
# print(results)

import os

def analyze_solidity_file(file_path, checks):
    with open(file_path, 'r') as f:
        code = f.read()

    findings = []

    # Execute each check and collect findings
    for check in checks:
        findings.extend(check(code))

    # Append filename to each finding
    file_name = os.path.basename(file_path)
    if not findings:
        return [f"{file_name}: no findings"]
    else:
        findings = [f"{file_name}: {finding}" for finding in findings]
        return findings



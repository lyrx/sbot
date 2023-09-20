import re

# Helper function to get line number
def get_line_number(code, index):
    return code.count('\n', 0, index) + 1

def check_outdated_versions(code):
    results = []
    outdated_versions = ['0.4.', '0.5.']
    for version in outdated_versions:
        match = re.search(version, code)
        if match:
            line_no = get_line_number(code, match.start())
            results.append(f"Warning (line {line_no}): The code seems to be using an outdated Solidity version ({version}x).")
    return results

def check_pragma_experimental(code):
    match = re.search('pragma experimental', code)
    if match:
        line_no = get_line_number(code, match.start())
        return [f"Warning (line {line_no}): The code uses 'pragma experimental'. This can introduce instability."]
    return []

def check_send_transfer(code):
    send_transfer_pattern = re.compile(r'\.send\(|\.transfer\(')
    match = send_transfer_pattern.search(code)
    if match:
        line_no = get_line_number(code, match.start())
        return [f"Warning (line {line_no}): 'send' or 'transfer' detected. Ensure you handle their potential failures."]
    return []

def check_low_level_call(code):
    match = re.search(r'\.call\(', code)
    if match:
        line_no = get_line_number(code, match.start())
        return [f"Warning (line {line_no}): Low-level calls can be dangerous. Ensure you handle their potential failures and avoid reentrancy attacks."]
    return []

def check_tx_origin(code):
    match = re.search('tx.origin', code)
    if match:
        line_no = get_line_number(code, match.start())
        return [f"Warning (line {line_no}): 'tx.origin' detected. It can be manipulated by malicious contracts. Consider using 'msg.sender' instead."]
    return []

def check_visibility_specifiers(code):
    results = []
    visibility_specifiers = ['public', 'private', 'internal', 'external']
    function_pattern = re.compile(r'function\s+(\w+)\s*\(')
    matches = function_pattern.finditer(code)
    for match in matches:
        function = match.group(1)
        if not any(vis in function for vis in visibility_specifiers):
            line_no = get_line_number(code, match.start())
            results.append(f"Warning (line {line_no}): The function '{function}' does not have a visibility specifier.")
    return results

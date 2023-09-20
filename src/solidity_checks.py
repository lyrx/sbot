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
            message = f"Warning: The code seems to be using an outdated Solidity version ({version}x)."
            results.append({'line': line_no, 'message': message})
    return results

def check_pragma_experimental(code):
    results = []
    match = re.search('pragma experimental', code)
    if match:
        line_no = get_line_number(code, match.start())
        message = "Warning: The code uses 'pragma experimental'. This can introduce instability."
        results.append({'line': line_no, 'message': message})
    return results

def check_send_transfer(code):
    results = []
    send_transfer_pattern = re.compile(r'\.send\(|\.transfer\(')
    match = send_transfer_pattern.search(code)
    if match:
        line_no = get_line_number(code, match.start())
        message = "Warning: 'send' or 'transfer' detected. Ensure you handle their potential failures."
        results.append({'line': line_no, 'message': message})
    return results

def check_low_level_call(code):
    results = []
    match = re.search(r'\.call\(', code)
    if match:
        line_no = get_line_number(code, match.start())
        message = "Warning: Low-level calls can be dangerous. Ensure you handle their potential failures and avoid reentrancy attacks."
        results.append({'line': line_no, 'message': message})
    return results

def check_tx_origin(code):
    results = []
    match = re.search('tx.origin', code)
    if match:
        line_no = get_line_number(code, match.start())
        message = "Warning: 'tx.origin' detected. It can be manipulated by malicious contracts. Consider using 'msg.sender' instead."
        results.append({'line': line_no, 'message': message})
    return results

def check_visibility_specifiers(code):
    results = []
    visibility_specifiers = ['public', 'private', 'internal', 'external']
    function_pattern = re.compile(r'function\s+(\w+)\s*\(')
    matches = function_pattern.finditer(code)
    for match in matches:
        function = match.group(1)
        if not any(vis in function for vis in visibility_specifiers):
            line_no = get_line_number(code, match.start())
            message = f"Warning: The function '{function}' does not have a visibility specifier."
            results.append({'line': line_no, 'message': message})
    return results

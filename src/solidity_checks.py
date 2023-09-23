import re

# Helper function to get line number
def get_line_number(code, index):
    return code.count('\n', 0, index) + 1

def check_outdated_versions(code):
    results = []
    outdated_versions = ['0.4.', '0.5.']
    for version in outdated_versions:
        for match in re.finditer(version, code):
            line_no = get_line_number(code, match.start())
            message = f"Warning: The code seems to be using an outdated Solidity version ({version}x)."
            results.append({'line': line_no, 'message': message})
    return results

def check_pragma_experimental(code):
    results = []
    for match in re.finditer('pragma experimental', code):
        line_no = get_line_number(code, match.start())
        message = "Warning: The code uses 'pragma experimental'. This can introduce instability."
        results.append({'line': line_no, 'message': message})
    return results

def check_send_transfer(code):
    results = []
    send_transfer_pattern = re.compile(r'\.send\(|\.transfer\(')
    for match in send_transfer_pattern.finditer(code):
        line_no = get_line_number(code, match.start())
        message = "Warning: 'send' or 'transfer' detected. Ensure you handle their potential failures."
        results.append({'line': line_no, 'message': message})
    return results

def check_low_level_call(code):
    results = []
    for match in re.finditer(r'\.call\(', code):
        line_no = get_line_number(code, match.start())
        message = "Warning: Low-level calls can be dangerous. Ensure you handle their potential failures and avoid reentrancy attacks."
        results.append({'line': line_no, 'message': message})
    return results

def check_tx_origin(code):
    results = []
    for match in re.finditer('tx.origin', code):
        line_no = get_line_number(code, match.start())
        message = "Warning: 'tx.origin' detected. It can be manipulated by malicious contracts. Consider using 'msg.sender' instead."
        results.append({'line': line_no, 'message': message})
    return results

def check_visibility_specifiers(code):
    results = []
    visibility_specifiers = ['public', 'private', 'internal', 'external']
    function_pattern = re.compile(r'function\s+(\w+)\s*\(')
    for match in function_pattern.finditer(code):
        function = match.group(1)
        if not any(vis in function for vis in visibility_specifiers):
            line_no = get_line_number(code, match.start())
            message = f"Warning: The function '{function}' does not have a visibility specifier."
            results.append({'line': line_no, 'message': message})
    return results


import re

def check_storage_initialization(code):
    """
    Checks for storage variable initializations in Solidity code that go from zero to non-zero.

    Initializing a storage variable is one of the most expensive operations a contract can do.
    When a storage variable goes from zero to non-zero, the user must pay 22,100 gas total
    (20,000 gas for a zero to non-zero write and 2,100 for a cold storage access).
    This is why the Openzeppelin reentrancy guard registers functions as active or not with
    1 and 2 rather than 0 and 1. It only costs 5,000 gas to alter a storage variable from
    non-zero to non-zero.

    Parameters:
    - code (str): The Solidity code to be checked.

    Returns:
    - list: A list of warnings with line numbers where storage variables are initialized to non-zero values.
    """

    results = []

    # Pattern to match storage variable declarations
    storage_var_pattern = re.compile(r'(uint[0-9]*|int[0-9]*|address|bool|string|bytes[0-9]*)\s+([\w_]+);')
    storage_vars = [match.group(2) for match in storage_var_pattern.finditer(code)]

    # Check if any storage variable is initialized to non-zero in the code
    for var in storage_vars:
        non_zero_init_pattern = re.compile(rf'{var}\s*=\s*[^0\s;]+;')
        for match in non_zero_init_pattern.finditer(code):
            line_no = get_line_number(code, match.start())
            message = f"Warning: The storage variable '{var}' is initialized to a non-zero value. This can be expensive in terms of gas."
            results.append({'line': line_no, 'message': message})

    return results



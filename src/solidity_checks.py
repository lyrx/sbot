import regex as re



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
def check_storage_initialization(code):
    results = []

    # Pattern to match storage variable declarations
    storage_var_pattern = re.compile(r'(uint[0-9]*|int[0-9]*|address|bool|string|bytes[0-9]*)\s+(public)?\s+([\w_]+);')
    storage_vars = [match.group(3) for match in storage_var_pattern.finditer(code)]

    # Pattern to match function bodies, excluding the outermost curly braces
    function_body_pattern = re.compile(r'\bfunction\b[^{]*{((?:[^{}]|(?R))*)}', re.DOTALL)
    function_bodies_matches = [match for match in function_body_pattern.finditer(code)]

    # Check if any storage variable is initialized to non-zero inside function bodies
    for var in storage_vars:
        non_zero_init_pattern = re.compile(rf'{var}\s*=\s*[^0\s;]+;')
        for match in function_bodies_matches:
            body = match.group(1)
            for init_match in non_zero_init_pattern.finditer(body):
                # Adjust the line number calculation to account for the start of the function body
                line_no = get_line_number(code, init_match.start() + match.start(1))
                message = f"Warning: The storage variable '{var}' is set inside a function. This can be expensive in terms of gas."
                results.append({'line': line_no, 'message': message})

    return results

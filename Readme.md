![](images/sbot.png)

# SBOT CODALYZER
## THE Source Code Analyzer

This project provides an extensible static analyzer for Source code to identify common patterns
that might indicate potential security vulnerabilities.
The analyzer is written in Python and is designed for easy extensibility with additional checks.

## Features

- Detects usage of outdated Solidity compiler versions.
- Identifies the use of pragma experimental.
- Checks for potential unlocked ether due to unchecked send or transfer.
- Warns about low-level .call() usage.
- Highlights potential misuse of tx.origin instead of msg.sender.
- Verifies the presence of function visibility specifiers.

## Setup

1. Clone this repository to your local machine.
2. Ensure you have Python 3.x installed.
3. [Optional] Set up a virtual environment for the project.

## Usage

### Analyzing a Single Source File

1. Place the Source code you want to analyze in a .sol file.
2. Use the provided shell script to run the analyzer, providing the path to the Source file:

`./analyze_file.sh </path/to/your/file.sol>`

3. Review the output for any potential warnings or issues identified by the analyzer.

### Analyzing a Directory of Source Files

1. Ensure all the Source files you want to analyze are within a directory.
2. Use the provided shell script to run the analyzer, providing the path to the directory:

`./analyze_dir.sh </path/to/your/directory/>`

3. Review the output for any potential warnings or issues identified by the analyzer for each file.



## Extending the  Analyzer

The Source Analyzer is structured for easy extensibility. The core checks are stored in the `check_structures` dictionary. Within this dictionary, the "initial" key points to a list of checks. Each check is a dictionary containing two key-value pairs: "name" and "func".

### Steps to Add a New Check:

1. **Write the Check Function**: Create a new function in `solidity_checks.py`. This function should accept the Source code as a string argument and return a list of findings.

   Example:
   ```def new_check_function(code_string):
       # Your check logic here
       return findings```

2. **Import the Check Function**: At the beginning of your main script (or wherever `check_structures` is defined), import your new check function:

   ```from solidity_checks import new_check_function```

3. **Add the Check to the Structure**: Extend the `check_structures` dictionary by adding a new dictionary to the list associated with the "initial" key:

   ```{"name": "Descriptive Name of the Check", "func": new_check_function}```

By following these steps, your new check will be integrated into the analyzer and will be executed when the script runs.

## Contributing

Contributions to improve the analyzer or add more checks are welcome! Please submit a pull request with your changes.

## Disclaimer

This tool provides basic static analysis of Solidity code for potential vulnerabilities. It is not a substitute for thorough manual code review or dynamic analysis. Always consult with blockchain security experts when developing and deploying smart contracts.

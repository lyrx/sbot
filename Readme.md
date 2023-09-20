# Solidity Code Analyzer

This project provides a simple static analyzer for Solidity code to identify common patterns that might indicate potential security vulnerabilities. The analyzer is written in Python and is designed for easy extensibility with additional checks.

## Features

- Detects usage of outdated Solidity compiler versions.
- Identifies the use of `pragma experimental`.
- Checks for potential unlocked ether due to unchecked `send` or `transfer`.
- Warns about low-level `.call()` usage.
- Highlights potential misuse of `tx.origin` instead of `msg.sender`.
- Verifies the presence of function visibility specifiers.

## Setup

1. Clone this repository to your local machine.
2. Ensure you have Python 3.x installed.
3. [Optional] Set up a virtual environment for the project.

## Usage

1. Place the Solidity code you want to analyze in a `.sol` file.
2. Run the main Python script, providing the path to the Solidity file:

```bash
python main.py /path/to/your/file.sol
```

3. Review the output for any potential warnings or issues identified by the analyzer.

## Extending the Analyzer

To add more checks:

1. Create a new function in `solidity_checks.py`.
2. Ensure your function accepts the Solidity code as a string argument and returns a list of findings.
3. Import and add your new check function to the `checks` list in `main.py`.

## Contributing

Contributions to improve the analyzer or add more checks are welcome! Please submit a pull request with your changes.

## Disclaimer

This tool provides basic static analysis of Solidity code for potential vulnerabilities. It is not a substitute for thorough manual code review or dynamic analysis. Always consult with blockchain security experts when developing and deploying smart contracts.

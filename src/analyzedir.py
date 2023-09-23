import sys
from solidity_analyzer import analyze_solidity_dir
from bloodhounds import check_structures

def handle_parameters():
    """
    Handle command-line parameters and return the base path, key, and optional GitHub directory.

    Returns:
    - tuple: A tuple containing the base path, key, and optional GitHub directory.
    """
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: python analyzedir.py <base_path> <key> [githubDir]")
        sys.exit(1)

    base_path = sys.argv[1]
    key = sys.argv[2]

    if key not in check_structures:
        print(f"Key '{key}' not found in check_structures.")
        sys.exit(1)

    githubDir = None
    if len(sys.argv) == 4:
        githubDir = sys.argv[3]

    return base_path, key, githubDir

def display_analysis(results, base_path, githubDir=None):
    """
    Display the analysis results for each file.

    Parameters:
    - results (dict): A dictionary containing file paths as keys and their corresponding analysis as values.
    - base_path (str): The base path for the analysis.
    - githubDir (str, optional): The path to the sources on GitHub.
    """
    for file_path, analysis in results.items():
        # Compute the RELATIVE_PATH
        relative_path = file_path.replace(base_path, '').lstrip('/')

        # Only process and print results if the analysis for the file has content
        if len(analysis) > 0:
            print(f"File: {file_path}")
            for i in range(len(analysis)):
                cn = analysis[i]["check_name"]
                msg = analysis[i]["message"]
                line = analysis[i]["line"]
                # Construct the link to the source line in GitHub
                if githubDir:
                    github_link = f"{githubDir}/{relative_path}#L{line}"
                    print(f"Source Link: {github_link}")
                print(f"{cn}: {msg} (Line {line})")

            print("-" * 50)  # Separator line for clarity

def main():
    base_path, key, githubDir = handle_parameters()
    results = analyze_solidity_dir(base_path, check_structures[key])
    display_analysis(results, base_path, githubDir)

if __name__ == "__main__":
    main()

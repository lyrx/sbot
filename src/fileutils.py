import os

def findpaths(base_directory, file_ending):
    """
    Traverses a base directory recursively and collects all files matching the given ending.

    Parameters:
    - base_directory (str): The directory to start the search from.
    - file_ending (str): The file ending to match (e.g., '.sol').

    Returns:
    - list: A list of full paths to files that match the given ending.
    """

    matching_files = []

    for dirpath, dirnames, filenames in os.walk(base_directory):
        for filename in filenames:
            if filename.endswith(file_ending):
                full_path = os.path.join(dirpath, filename)
                matching_files.append(full_path)

    return matching_files

# Example usage:
# paths = findpaths('/path/to/base/directory', '.sol')
# print(paths)

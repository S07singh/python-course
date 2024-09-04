import os

def print_directory_contents(path):
    # List all files and directories in the given path
    for item in os.listdir(path):
        print(item)

# Example usage:
directory_path = '/'  # Replace with your directory path
print(f"Contents of directory '{directory_path}':")
print_directory_contents(directory_path)

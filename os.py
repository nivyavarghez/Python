import os

def create_directory(directory):
    try:
        os.makedirs(directory)
        print(f"Directory '{directory}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

def list_directory(directory):
    try:
        files = os.listdir(directory)
        print(f"Contents of directory '{directory}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Directory '{directory}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def search_py_files(directory):
    try:
        py_files = [f for f in os.listdir(directory) if f.endswith('.py')]
        print(f".py files in directory '{directory}':")
        for file in py_files:
            print(file)
    except FileNotFoundError:
        print(f"Directory '{directory}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def remove_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' removed successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory = 'test_directory'
file_path = 'test_directory/test_file.txt'

# Create a directory
create_directory(directory)

# Create a test file in the directory for demonstration
with open(file_path, 'w') as f:
    f.write('This is a test file.')

# List contents of the directory
list_directory(directory)

# Search for .py files in the directory
search_py_files(directory)

# Remove a particular file
remove_file(file_path)

# List contents of the directory again to verify file removal
list_directory(directory)

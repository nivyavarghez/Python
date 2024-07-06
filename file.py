def copy_file_line_by_line(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            with open(destination_file, 'w') as dest:
                for line in src:
                    dest.write(line)
        print(f"Contents of {source_file} have been copied to {destination_file} successfully.")
    except FileNotFoundError:
        print(f"The file {source_file} does not exist.")
    except IOError as e:
        print(f"An IOError occurred: {e}")

# Example usage
source_file = 'c.txt'
destination_file = 'd.txt'
copy_file_line_by_line(source_file, destination_file)

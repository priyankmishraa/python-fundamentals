# Script: Reading and Writing Operations on File

# Explanation: File Operations with open() and close()
# The open() function is used to open a file, and close() is used to close it.
# Different modes (e.g., 'r', 'w', 'a') are specified to indicate the purpose of file access.

# Example 1: Reading from a Text File
def read_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError as e:
        return f"Error: {e}"

# Example 2: Writing to a Text File
def write_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return f"Content written to {file_path}"
    except Exception as e:
        return f"Error: {e}"

# Example 3: Appending to a Text File
def append_to_file(file_path, content):
    try:
        with open(file_path, 'a') as file:
            file.write(content)
        return f"Content appended to {file_path}"
    except Exception as e:
        return f"Error: {e}"

# Uncomment the lines below to see the behavior of different examples
# content = read_from_file("example.txt")
# result1 = write_to_file("new_file.txt", "Hello, World!")
# result2 = append_to_file("existing_file.txt", "\nAppended content.")

# Example 4: Reading and Writing Binary Files
def read_write_binary_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            # Reading binary data
            binary_data = file.read()
        
        # Modifying the binary data (e.g., reversing bytes)
        modified_data = binary_data[::-1]

        with open("modified_binary_file.txt", 'wb') as modified_file:
            # Writing modified binary data to a new file
            modified_file.write(modified_data)

        return "Binary file read, modified, and written to 'modified_binary_file.txt'"
    except Exception as e:
        return f"Error: {e}"

# Uncomment the line below to see the behavior of the binary file example
# result3 = read_write_binary_file("binary_file.bin")

# --------------------
# OUTPUT
# --------------------

# Content written to new_file.txt
# Content appended to existing_file.txt

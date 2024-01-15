# Script: Error Handling in File Operations

# Explanation: Error Handling during File Operations
# Proper error handling is crucial for dealing with potential issues during file reading and writing.

# Example 1: Handling File Not Found Error during Reading
def read_file_with_error_handling(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError as e:
        return f"Error: {e}"

# Uncomment the line below to see the behavior of handling File Not Found Error during reading
# file_content_with_error_handling = read_file_with_error_handling("nonexistent_file.txt")

# Example 2: Handling Permission Error during Writing
def write_to_file_with_error_handling(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return f"Content written to {file_path}"
    except PermissionError as e:
        return f"Error: {e}"

# Uncomment the line below to see the behavior of handling Permission Error during writing
# write_result_with_error_handling = write_to_file_with_error_handling("/etc/some_protected_file.txt", "Hello!")

# Example 3: Handling Multiple Errors during Reading
def read_file_with_multiple_error_handling(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            # Simulating an exception
            int(content)  # This line will raise a ValueError
        return content
    except FileNotFoundError as e:
        return f"Error: {e}"
    except ValueError as e:
        return f"Error: {e}"

# Uncomment the line below to see the behavior of handling multiple errors during reading
# content_with_multiple_error_handling = read_file_with_multiple_error_handling("nonexistent_file.txt")

# Example 4: Handling Errors during Writing with Context Manager
def write_with_error_handling_using_context(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return f"Content written to {file_path}"
    except Exception as e:
        return f"Error: {e}"
    finally:
        print("This block will execute whether an exception occurs or not.")

# Uncomment the line below to see the behavior of handling errors during writing with context manager
# write_result_with_context_error_handling = write_with_error_handling_using_context("/etc/some_protected_file.txt", "Hello!")


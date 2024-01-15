# Script: Writing Text to a File in Python

# Explanation: Writing Text to a File
# Python provides different methods for writing text to a file, including writing single lines, multiple lines, and using various features.

# Example 1: Writing a Single Line to a File
def write_single_line(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return f"Content written to {file_path}"
    except Exception as e:
        return f"Error: {e}"

# Example 2: Writing Multiple Lines to a File
def write_multiple_lines(file_path, lines):
    try:
        with open(file_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')  # Adding newline character after each line
        return f"Content written to {file_path}"
    except Exception as e:
        return f"Error: {e}"

# Example 3: Appending Text to an Existing File
def append_to_existing_file(file_path, content):
    try:
        with open(file_path, 'a') as file:
            file.write(content)
        return f"Content appended to {file_path}"
    except Exception as e:
        return f"Error: {e}"

# Example 4: Using write() and writelines() Methods
def write_with_methods(file_path, lines):
    try:
        with open(file_path, 'w') as file:
            file.write("Using write() method:\n")
            file.write(lines[0] + '\n')

            file.write("\nUsing writelines() method:\n")
            file.writelines(lines[1:])
        return f"Content written to {file_path}"
    except Exception as e:
        return f"Error: {e}"

# Uncomment the lines below to see the behavior of different examples
# result1 = write_single_line("single_line.txt", "Hello, World!")
# result2 = write_multiple_lines("multiple_lines.txt", ["Line 1", "Line 2", "Line 3"])
# result3 = append_to_existing_file("existing_file.txt", "\nAppended content.")
# result4 = write_with_methods("methods_example.txt", ["First line", "Second line", "Third line"])


# --------------------
# OUTPUT
# --------------------

# Content written to single_line.txt
# Content written to multiple_lines.txt
# Content appended to existing_file.txt
# Content written to methods_example.txt

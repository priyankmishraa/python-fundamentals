# Script: File Reading Methods in Python

# Explanation: File Reading Methods
# Python provides different methods (e.g., read(), readline(), readlines()) for reading content from a file.

# Example 1: Using read() to Read the Entire File
def read_entire_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError as e:
        return f"Error: {e}"

# Example 2: Using readline() to Read a Single Line
def read_single_line(file_path):
    try:
        with open(file_path, 'r') as file:
            first_line = file.readline()
        return first_line
    except FileNotFoundError as e:
        return f"Error: {e}"

# Example 3: Using readlines() to Read All Lines into a List
def read_all_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError as e:
        return f"Error: {e}"

# Uncomment the lines below to see the behavior of different examples
# result1 = read_entire_file("example.txt")
# result2 = read_single_line("example.txt")
# result3 = read_all_lines("example.txt")

# Example 4: Iterating Over Lines with a for Loop
def iterate_over_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())  # Stripping newline characters for better output
        return "Iteration completed"
    except FileNotFoundError as e:
        return f"Error: {e}"

# Uncomment the line below to see the behavior of the iteration example
# result4 = iterate_over_lines("example.txt")


# --------------------
# OUTPUT
# --------------------

# Line 1
# Line 2
# Line 3

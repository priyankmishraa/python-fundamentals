# Script: Difference Between Syntax Errors and Exceptions

# Explanation: Syntax Errors
# Syntax errors occur during the parsing (compilation) stage. They are related to incorrect Python syntax.

# Example 1: Syntax Error
# Uncomment the line below to see a syntax error
# print("Hello, World!"

# Explanation: Exceptions
# Exceptions occur during the runtime (execution) stage. They are related to logical errors, unexpected situations, or issues that arise during the execution of the program.

# Example 2: ZeroDivisionError (Exception)
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        return f"Error: {e}"

# Example 3: Handling IndexError (Exception)
def access_list_element(my_list, index):
    try:
        value = my_list[index]
        return value
    except IndexError as e:
        return f"Error: {e}"

# Example 4: Handling FileNotFoundError (Exception)
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError as e:
        return f"Error: {e}"

# Example 5: Handling Multiple Exceptions
def perform_operation(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError as e:
        return f"Error: Division by zero ({e})"
    except TypeError as e:
        return f"Error: Invalid operation ({e})"
    except Exception as e:
        return f"Error: {e}"

# Uncomment the line below to see an IndexError exception
# access_list_element([1, 2, 3], 5)

# Uncomment the line below to see a FileNotFoundError exception
# read_file("nonexistent_file.txt")

# Uncomment the line below to see a ZeroDivisionError exception
# result = divide_numbers(5, 0)

# Uncomment the line below to see a TypeError exception
# result = perform_operation(10, "2")


# --------------------
# OUTPUT
# --------------------

# Error: division by zero
# Error: list index out of range
# Error: [Errno 2] No such file or directory: 'nonexistent_file.txt'
# Error: invalid operation

# Script: Built-In Exceptions in Python

# Explanation: Built-In Exceptions
# Python provides a variety of built-in exceptions to handle different error conditions during program execution.

# Example 1: ZeroDivisionError
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        return f"Error: {e}"

# Example 2: IndexError
def access_list_element(my_list, index):
    try:
        value = my_list[index]
        return value
    except IndexError as e:
        return f"Error: {e}"

# Example 3: FileNotFoundError
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError as e:
        return f"Error: {e}"

# Example 4: TypeError
def perform_operation(x, y):
    try:
        result = x / y
        return result
    except TypeError as e:
        return f"Error: {e}"

# Example 5: ValueError
def convert_to_int(value):
    try:
        integer_value = int(value)
        return integer_value
    except ValueError as e:
        return f"Error: {e}"

# Example 6: AssertionError
def assert_condition(value):
    try:
        assert value, "Assertion failed"
        return "Assertion passed"
    except AssertionError as e:
        return f"Error: {e}"

# Example 7: KeyError
def access_dictionary_key(my_dict, key):
    try:
        value = my_dict[key]
        return value
    except KeyError as e:
        return f"Error: {e}"

# Example 8: FileExistsError
def create_file(file_path):
    try:
        with open(file_path, 'x'):
            pass  # Creating an empty file
        return f"File created: {file_path}"
    except FileExistsError as e:
        return f"Error: {e}"

# Example 9: NotImplementedError
def custom_function():
    raise NotImplementedError("This function is not implemented yet")

# Uncomment the line below to see a NotImplementedError exception
# custom_function()



# --------------------
# OUTPUT
# --------------------

# Error: division by zero
# Error: list index out of range
# Error: [Errno 2] No such file or directory: 'nonexistent_file.txt'
# Error: unsupported operand type(s) for /: 'str' and 'str'
# Error: invalid literal for int() with base 10: 'abc'
# Error: Assertion failed
# Error: 'age'
# Error: [Errno 17] File exists: 'existing_file.txt'
# Error: This function is not implemented yet

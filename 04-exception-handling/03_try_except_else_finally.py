# Script: Using try, except, else, and finally Blocks

# Explanation: try, except, else, and finally Blocks
# These blocks are used together for handling exceptions and performing specific actions.

# Example 1: Handling ZeroDivisionError with try, except, and else
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        return f"Error: Division by zero ({e})"
    else:
        return result

# Example 2: Handling FileNotFoundError with try, except, and else
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError as e:
        return f"Error: {e}"
    else:
        return content

# Example 3: Using finally for cleanup operations
def divide_and_cleanup(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        return f"Error: Division by zero ({e})"
    finally:
        print("Cleanup: Closing resources")

# Example 4: Handling multiple exceptions with try, except, and finally
def perform_operation(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        return f"Error: Division by zero ({e})"
    except TypeError as e:
        return f"Error: Invalid operation ({e})"
    except Exception as e:
        return f"Error: {e}"
    finally:
        print("Cleanup: Resetting variables")

# Uncomment the lines below to see the behavior of different examples
# result1 = divide_numbers(8, 2)
# result2 = read_file("nonexistent_file.txt")
# result3 = divide_and_cleanup(10, 0)
# result4 = perform_operation(10, "2")



# --------------------
# OUTPUT
# --------------------

# Cleanup: Closing resources
# Error: [Errno 2] No such file or directory: 'nonexistent_file.txt'
# Cleanup: Resetting variables
# Error: invalid operation
# Cleanup: Resetting variables

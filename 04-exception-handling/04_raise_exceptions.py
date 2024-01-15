# Script: Raising Exceptions in Python

# Explanation: Raising Exceptions
# The raise statement is used to raise exceptions in Python. It allows you to signal that an error or exceptional condition has occurred.

# Example 1: Raising a Custom Exception
def check_positive_number(value):
    if value <= 0:
        raise ValueError("Value must be a positive number")

# Example 2: Raising a Specific Exception Conditionally
def divide_numbers(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# Example 3: Raising an Exception in a Function
def perform_custom_operation(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both arguments must be integers")
    return x * y

# Uncomment the lines below to see the behavior of different examples
# check_positive_number(-5)
# result = divide_numbers(10, 0)
# result = perform_custom_operation(5, "2")



# --------------------
# OUTPUT
# --------------------

# ValueError: Value must be a positive number
# ZeroDivisionError: Cannot divide by zero
# TypeError: Both arguments must be integers

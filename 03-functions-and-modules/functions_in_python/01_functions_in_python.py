# Script: Functions in Python and Naming Conventions

# Explanation: Functions in Python
# Functions are blocks of reusable code that perform a specific task. They are defined using the def keyword.

# Example 1: Simple Function
def greet(name):
    """This function greets the user."""
    print(f"Hello, {name}!")

# Example 2: Function with Return Value
def square(x):
    """This function returns the square of a number."""
    return x ** 2

# Example 3: Function with Default Parameter
def power(base, exponent=2):
    """This function calculates the power of a number with an optional exponent."""
    return base ** exponent

# Example 4: Naming Conventions in Python
# Function names should be lowercase with words separated by underscores (snake_case).
# Docstrings should be used to provide documentation for the function.

# Example 5: Function Calls
# Calling the defined functions
greet("Alice")

num_squared = square(5)
print(f"Square of 5: {num_squared}")

result_power = power(2)
print(f"2 to the power of 2: {result_power}")

result_custom_power = power(2, 3)
print(f"2 to the power of 3: {result_custom_power}")



# --------------------
# OUTPUT
# --------------------

# Hello, Alice!
# Square of 5: 25
# 2 to the power of 2: 4
# 2 to the power of 3: 8


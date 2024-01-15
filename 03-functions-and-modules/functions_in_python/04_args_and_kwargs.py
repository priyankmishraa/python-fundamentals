
# Script: *args and **kwargs in Python Functions

# Explanation: *args and **kwargs
# *args allows a function to accept any number of positional arguments.
# **kwargs allows a function to accept any number of keyword arguments.

# Example 1: Function with *args
def add_numbers(*args):
    """This function adds a variable number of numbers."""
    result = 0
    for num in args:
        result += num
    return result

# Example 2: Function with **kwargs
def display_info(**kwargs):
    """This function displays information using keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example 3: Calling Functions with *args and **kwargs
result_sum = add_numbers(1, 2, 3, 4, 5)
print(f"Sum of numbers: {result_sum}")

display_info(name="Alice", age=25, city="Wonderland")


# --------------------
# OUTPUT
# --------------------

# Sum of numbers: 15
# name: Alice
# age: 25
# city: Wonderland

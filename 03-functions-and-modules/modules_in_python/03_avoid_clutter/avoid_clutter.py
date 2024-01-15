# Example 2: Avoiding Namespace Clutter
# Save this code in a file named "avoid_clutter.py"

# avoid_clutter.py
from math_operations import add as add_numbers, multiply as multiply_numbers

# Using the specific functions with new names
result_clutter_add = add_numbers(3, 7)
result_clutter_multiply = multiply_numbers(4, 5)

# Displaying results
print("Avoiding Clutter - Addition:", result_clutter_add)
print("Avoiding Clutter - Multiplication:", result_clutter_multiply)

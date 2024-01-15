# Example 2: Using the Module in Another Script
# Save this code in a file named "main_script.py"

# main_script.py
import math_operations

# Using functions from the module
result_add = math_operations.add(5, 3)
result_subtract = math_operations.subtract(8, 4)
result_multiply = math_operations.multiply(2, 6)
result_divide = math_operations.divide(10, 2)

# Displaying results
print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)

# Example 3: Importing Specific Functions from a Module
# Save this code in a file named "specific_import.py"

# specific_import.py
from math_operations import add, multiply

# Using the imported functions
result_specific_add = add(3, 7)
result_specific_multiply = multiply(4, 5)

# Displaying results
print("Specific Import - Addition:", result_specific_add)
print("Specific Import - Multiplication:", result_specific_multiply)

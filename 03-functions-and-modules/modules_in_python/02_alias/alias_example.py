# Script: Module Aliasing and Avoiding Namespace Clutter

# Explanation: Module Aliasing
# Module aliasing involves creating a shorter or more convenient alias for a module when importing.

# Example 1: Module Aliasing
# Save this code in a file named "alias_example.py"

# alias_example.py
import math_operations as ops

# Using the aliased module
result_alias_add = ops.add(5, 3)
result_alias_multiply = ops.multiply(2, 6)

# Displaying results
print("Aliased Module - Addition:", result_alias_add)
print("Aliased Module - Multiplication:", result_alias_multiply)


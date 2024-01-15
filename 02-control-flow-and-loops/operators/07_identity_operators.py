# Script: Understanding Identity Operators in Python

# Explanation: Identity Operators
# Identity operators compare the memory location of two objects.

# Example 1: is Operator
x = [1, 2, 3]
y = [1, 2, 3]

# Check if x and y refer to the same object
is_same_object = x is y
print("Are x and y the same object?", is_same_object)

# Example 2: is not Operator
a = 10
b = 10

# Check if a and b do not refer to the same object
is_not_same_object = a is not b
print("Are a and b not the same object?", is_not_same_object)

# Example 3: Identity Operators with None
variable = None

# Check if variable is None
is_none = variable is None
print("Is variable None?", is_none)

# Check if variable is not None
is_not_none = variable is not None
print("Is variable not None?", is_not_none)



# --------------------
# OUTPUT
# --------------------
# Are x and y the same object? False
# Are a and b not the same object? False
# Is variable None? True
# Is variable not None? False

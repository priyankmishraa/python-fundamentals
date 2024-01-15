# Script: Diving into the `type()` Function in Python

# Explanation: Using the type() Function
# The type() function is used to get the type of an object or a value.

# Example 1: Using type() with different data types
integer_variable = 42
float_variable = 3.14
string_variable = "Python"
list_variable = [1, 2, 3]
tuple_variable = (4, 5, 6)
boolean_variable = True

print("Type of integer_variable:", type(integer_variable))
print("Type of float_variable:", type(float_variable))
print("Type of string_variable:", type(string_variable))
print("Type of list_variable:", type(list_variable))
print("Type of tuple_variable:", type(tuple_variable))
print("Type of boolean_variable:", type(boolean_variable))

# Explanation: Dynamic Typing in Python
# Python is dynamically typed, meaning the type of a variable is determined at runtime.

# Example 2: Dynamic Typing
dynamic_variable = 10
print("Type of dynamic_variable initially:", type(dynamic_variable))

dynamic_variable = "Python"
print("Type of dynamic_variable after reassignment:", type(dynamic_variable))

# --------------------
# OUTPUT
# --------------------

# Type of integer_variable: <class 'int'>
# Type of float_variable: <class 'float'>
# Type of string_variable: <class 'str'>
# Type of list_variable: <class 'list'>
# Type of tuple_variable: <class 'tuple'>
# Type of boolean_variable: <class 'bool'>
# Type of dynamic_variable initially: <class 'int'>
# Type of dynamic_variable after reassignment: <class 'str'>

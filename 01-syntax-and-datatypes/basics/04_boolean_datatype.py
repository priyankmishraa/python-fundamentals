# Script: Decoding Boolean Data Types in Python

# Explanation: Boolean Data Type
# Booleans represent truth values, either True or False.

# Example 1: Boolean Variables
is_python_fun = True
is_learning = False

print("Is Python fun?", is_python_fun)
print("Is learning Python fun?", is_learning)

# Explanation: Comparison Operators
# Comparison operators evaluate expressions and return boolean results.

# Example 2: Comparison Operators
x = 10
y = 5

greater_than = x > y
less_than = x < y
equal_to = x == y
not_equal_to = x != y

print("Is x greater than y?", greater_than)
print("Is x less than y?", less_than)
print("Is x equal to y?", equal_to)
print("Is x not equal to y?", not_equal_to)

# Explanation: Logical Operators
# Logical operators perform logical operations on boolean values.

# Example 3: Logical Operators
is_sunny = True
is_warm = False

# Logical AND
both_conditions_met = is_sunny and is_warm
print("Is it sunny and warm?", both_conditions_met)

# Logical OR
either_condition_met = is_sunny or is_warm
print("Is it either sunny or warm?", either_condition_met)

# Logical NOT
not_sunny = not is_sunny
print("Is it not sunny?", not_sunny)

# --------------------
# OUTPUT
# --------------------

# Is Python fun? True
# Is learning Python fun? False
# Is x greater than y? True
# Is x less than y? False
# Is x equal to y? False
# Is x not equal to y? True
# Is it sunny and warm? False
# Is it either sunny or warm? True
# Is it not sunny? False

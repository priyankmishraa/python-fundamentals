
# Script: Understanding Membership Operators in Python

# Explanation: Membership Operators
# Membership operators test whether a value is a member of a sequence.

# Example 1: In Operator
fruits = ['apple', 'banana', 'cherry']

# Check if 'banana' is in the list
is_banana_in_list = 'banana' in fruits
print("Is 'banana' in the list?", is_banana_in_list)

# Check if 'orange' is not in the list
is_orange_not_in_list = 'orange' not in fruits
print("Is 'orange' not in the list?", is_orange_not_in_list)

# Example 2: In Operator with Strings
sentence = "Python is a powerful language."

# Check if 'powerful' is in the string
is_powerful_in_string = 'powerful' in sentence
print("Is 'powerful' in the string?", is_powerful_in_string)

# Check if 'Java' is not in the string
is_java_not_in_string = 'Java' not in sentence
print("Is 'Java' not in the string?", is_java_not_in_string)


# --------------------
# OUTPUT
# --------------------

# Is 'banana' in the list? True
# Is 'orange' not in the list? True
# Is 'powerful' in the string? True
# Is 'Java' not in the string? True

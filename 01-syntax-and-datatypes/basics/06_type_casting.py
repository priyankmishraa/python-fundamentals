# Script: Demystifying Type Casting in Python

# Explanation: Implicit Type Conversion (Automatic)
# Python can automatically convert one data type to another if needed.

# Example 1: Implicit Type Conversion
integer_variable = 10
float_variable = 3.14

result = integer_variable + float_variable
print("Result of Implicit Type Conversion:", result)
print("Type of Result:", type(result))

# Explanation: Explicit Type Conversion (Manual)
# You can explicitly convert one data type to another using built-in functions.

# Example 2: Explicit Type Conversion (int(), float(), str())
float_to_int = int(3.99)
int_to_float = float(5)

string_to_int = int("42")
string_to_float = float("3.14")

print("Converted Float to Int:", float_to_int)
print("Converted Int to Float:", int_to_float)
print("Converted String to Int:", string_to_int)
print("Converted String to Float:", string_to_float)

# Example 3: Using str() for Concatenation
age = 25
message = "I am " + str(age) + " years old."
print(message)

# --------------------
# OUTPUT
# --------------------

# Result of Implicit Type Conversion: 13.14
# Type of Result: <class 'float'>
# Converted Float to Int: 3
# Converted Int to Float: 5.0
# Converted String to Int: 42
# Converted String to Float: 3.14
# I am 25 years old.

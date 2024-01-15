# Script: Unraveling Number Data Types in Python

# Explanation: Integer Data Type
# Integers are whole numbers without a fractional component.

# Example 1: Integer
my_integer = 42
print("Integer:", my_integer)

# Explanation: Float Data Type
# Floats are numbers that have a decimal point or are represented in exponential form.

# Example 2: Float
my_float = 3.14
print("Float:", my_float)

# Explanation: Complex Data Type
# Complex numbers have a real and an imaginary part, represented as x + yj, where x and y are floats.

# Example 3: Complex Number
my_complex = 2 + 3j
print("Complex Number:", my_complex)

# Explanation: Type Conversion
# You can convert between different number types using type casting.

# Example 4: Type Conversion
float_to_int = int(my_float)
int_to_float = float(my_integer)

print("Converted Float to Integer:", float_to_int)
print("Converted Integer to Float:", int_to_float)

# Explanation: Arithmetic Operations
# Perform basic arithmetic operations on numbers.

# Example 5: Arithmetic Operations
result_addition = my_integer + my_float
result_multiplication = my_integer * my_complex

print("Result of Addition:", result_addition)
print("Result of Multiplication:", result_multiplication)

# --------------------
# OUTPUT
# --------------------

# Integer: 42
# Float: 3.14
# Complex Number: (2+3j)
# Converted Float to Integer: 3
# Converted Integer to Float: 42.0
# Result of Addition: 45.14
# Result of Multiplication: (84+126j)

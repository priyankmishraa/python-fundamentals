
# Script: Exploring Bitwise Operators in Python

# Explanation: Bitwise Operators
# Bitwise operators perform operations on individual bits of binary representations of numbers.

# Example 1: Bitwise AND (&) Operator
a = 10  # Binary: 1010
b = 5   # Binary: 0101

bitwise_and_result = a & b
print("Bitwise AND Result:", bitwise_and_result)

# Example 2: Bitwise OR (|) Operator
bitwise_or_result = a | b
print("Bitwise OR Result:", bitwise_or_result)

# Example 3: Bitwise XOR (^) Operator
bitwise_xor_result = a ^ b
print("Bitwise XOR Result:", bitwise_xor_result)

# Example 4: Bitwise NOT (~) Operator
bitwise_not_a = ~a
print("Bitwise NOT of a:", bitwise_not_a)

# Example 5: Left Shift (<<) Operator
left_shift_result = a << 1
print("Left Shift Result:", left_shift_result)

# Example 6: Right Shift (>>) Operator
right_shift_result = a >> 1
print("Right Shift Result:", right_shift_result)


# --------------------
# OUTPUT
# --------------------

# Bitwise AND Result: 0
# Bitwise OR Result: 15
# Bitwise XOR Result: 15
# Bitwise NOT of a: -11
# Left Shift Result: 20
# Right Shift Result: 5

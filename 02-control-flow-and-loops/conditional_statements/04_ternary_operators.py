
# Script: Ternary Operator in Python

# Explanation: Ternary Operator
# The ternary operator provides a concise way to write a conditional expression in a single line.

# Example 1:
x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(f"The number {x} is {result}.")

# Example 2:
age = 25
status = "Adult" if age >= 18 else "Minor"
print(f"The person is a {status}.")

# Example 3: Nested Ternary Operator
score = 85
grade = "A" if score >= 90 else ("B" if score >= 80 else "C")
print(f"The student's grade is {grade}.")


# --------------------
# OUTPUT
# --------------------

# The number 10 is Even.
# The person is a Adult.
# The student's grade is A.

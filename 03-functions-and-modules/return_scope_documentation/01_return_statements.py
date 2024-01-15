# Script: Return Statement in Python Functions

# Explanation: Return Statement
# The return statement is used to send a value back from a function to the calling code.

# Example 1: Function with Simple Return
def add_numbers(a, b):
    """This function adds two numbers and returns the result."""
    return a + b

# Example 2: Function with Conditional Return
def get_grade(score):
    """This function returns the grade based on the given score."""
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

# Example 3: Function with Multiple Return Values
def calculate_stats(numbers):
    """This function calculates and returns multiple statistics."""
    total = sum(numbers)
    average = total / len(numbers)
    max_value = max(numbers)
    min_value = min(numbers)
    return total, average, max_value, min_value

# Example 4: Function with Early Return
def is_positive(number):
    """This function checks if a number is positive and returns a boolean."""
    if number > 0:
        return True
    else:
        return False

# Example 5: Function with No Return Statement (Implicitly returns None)
def no_return():
    """This function has no explicit return statement."""
    print("This function has no explicit return statement.")

# Example 6: Function Returning a Function
def get_operation(operator):
    """This function returns a specific operation function based on the operator."""
    if operator == '+':
        return lambda a, b: a + b
    elif operator == '*':
        return lambda a, b: a * b

# Example 7: Calling Functions with Return Statements
sum_result = add_numbers(5, 3)
print(f"Sum of numbers: {sum_result}")

grade = get_grade(75)
print(f"Grade: {grade}")

stats = calculate_stats([4, 7, 2, 9, 5])
print(f"Statistics: Total={stats[0]}, Average={stats[1]}, Max={stats[2]}, Min={stats[3]}")

positive_check = is_positive(8)
print(f"Is the number positive? {positive_check}")

no_return_result = no_return()
print(f"Result of function with no return: {no_return_result}")

add_operation = get_operation('+')
print(f"Result of addition operation: {add_operation(3, 4)}")

multiply_operation = get_operation('*')
print(f"Result of multiplication operation: {multiply_operation(3, 4)}")


# --------------------
# OUTPUT
# --------------------

# Sum of numbers: 8
# Grade: C
# Statistics: Total=27, Average=5.4, Max=9, Min=2
# Is the number positive? True
# This function has no explicit return statement.
# Result of function with no return: None
# Result of addition operation: 7
# Result of multiplication operation: 12

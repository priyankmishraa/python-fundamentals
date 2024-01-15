# Script: Parameters in Functions - Positional and Keyword Arguments

# Explanation: Parameters in Functions
# Parameters allow you to pass values to a function when it's called. There are two types of parameters: positional and keyword.

# Example 1: Function with Positional Parameters
def greet(name, greeting):
    """This function greets the user with a custom greeting."""
    print(f"{greeting}, {name}!")

# Example 2: Function with Keyword Parameters
def calculate_power(base, exponent):
    """This function calculates the power of a number using keyword parameters."""
    return base ** exponent

# Example 3: Function with Default Parameters
def power_with_default(base, exponent=2):
    """This function calculates the power of a number with an optional default exponent."""
    return base ** exponent

# Example 4: Calling Functions with Positional Arguments
greet("Alice", "Hello")

result_power = calculate_power(3, 4)
print(f"3 to the power of 4: {result_power}")

# Example 5: Calling Functions with Keyword Arguments
greet(greeting="Hi", name="Bob")

result_default_power = power_with_default(2)
print(f"2 to the power of 2 (default): {result_default_power}")

result_custom_power = power_with_default(2, exponent=3)
print(f"2 to the power of 3 (custom): {result_custom_power}")


# --------------------
# OUTPUT
# --------------------

# Hello, Alice!
# 3 to the power of 4: 81
# Hi, Bob!
# 2 to the power of 2 (default): 4
# 2 to the power of 3 (custom): 8

# Script: Default and Optional Parameters in Python Functions

# Explanation: Default and Optional Parameters
# Default parameters have predefined values and are used when no argument is provided for that parameter.

# Example 1: Function with Default Parameter
def greet(name, greeting="Hello"):
    """This function greets the user with a default greeting."""
    print(f"{greeting}, {name}!")

# Example 2: Function with Optional Parameter
def power_with_optional(base, exponent=None):
    """This function calculates the power of a number with an optional parameter."""
    if exponent is None:
        exponent = 2
    return base ** exponent

# Example 3: Calling Functions with Default and Optional Parameters
greet("Alice")
greet("Bob", greeting="Hi")

result_default_power = power_with_optional(3)
print(f"3 to the power of 2 (default): {result_default_power}")

result_custom_power = power_with_optional(3, exponent=4)
print(f"3 to the power of 4 (custom): {result_custom_power}")


# --------------------
# OUTPUT
# --------------------

# Hello, Alice!
# Hi, Bob!
# 3 to the power of 2 (default): 9
# 3 to the power of 4 (custom): 81


# Script: Custom Exceptions in Python

# Explanation: Custom Exceptions
# Custom exceptions are created by defining new exception classes that inherit from the built-in Exception class.

# Example 1: Creating a Custom Exception Class
class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative values are not allowed: {value}")

# Example 2: Using the Custom Exception
def check_positive_number(value):
    if value < 0:
        raise NegativeValueError(value)
    return f"Value {value} is positive"

# Example 3: Creating a Custom Exception with Additional Attributes
class CustomTypeError(Exception):
    def __init__(self, arg_name, arg_value, expected_type):
        self.arg_name = arg_name
        self.arg_value = arg_value
        self.expected_type = expected_type
        super().__init__(f"Invalid type for {arg_name}: {arg_value}. Expected {expected_type}")

# Example 4: Using the Custom Exception with Additional Attributes
def check_type(arg_name, arg_value, expected_type):
    if not isinstance(arg_value, expected_type):
        raise CustomTypeError(arg_name, arg_value, expected_type)
    return f"{arg_name} has the correct type"

# Uncomment the lines below to see the behavior of different examples
# result1 = check_positive_number(-5)
# result2 = check_type("count", "2", int)



# --------------------
# OUTPUT
# --------------------

# NegativeValueError: Negative values are not allowed: -5
# CustomTypeError: Invalid type for count: 2. Expected <class 'int'>

# Script: Documentation in Functions and Sphinx

# Explanation: Documentation in Functions
# Proper documentation helps others understand the purpose, parameters, and usage of functions.

# Example 1: Function with Docstring
def multiply(a, b):
    """
    This function multiplies two numbers.

    Parameters:
    - a (int): The first number.
    - b (int): The second number.

    Returns:
    int: The product of the two numbers.
    """
    return a * b

# Example 2: Function with Extended Docstring
def calculate_area(radius):
    """
    Calculate the area of a circle.

    Parameters:
    - radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    pi = 3.14159
    area = pi * radius**2
    return area

# Example 3: Function with Sphinx-Style Docstring
def divide(dividend, divisor):
    """
    Divide two numbers.

    :param float dividend: The number to be divided.
    :param float divisor: The divisor.

    :return: The result of the division.
    :rtype: float
    """
    if divisor == 0:
        raise ValueError("Cannot divide by zero.")
    return dividend / divisor

# Example 4: Use Sphinx to Generate Documentation
# Sphinx is a documentation generator that can be used to create documentation from docstrings.
# Install Sphinx using: pip install sphinx

# Example 5: Sphinx Configuration (conf.py)
# Create a Sphinx configuration file (conf.py) in your documentation directory.
# You can customize settings such as project name, author, and extensions.

# Example 6: Sphinx Build
# Run the following command in the terminal to build the documentation:
# sphinx-build -b html sourcedir builddir

# Example 7: View Sphinx Documentation
# Open the generated HTML documentation in the specified builddir.

# Note: Sphinx can generate documentation in various formats (HTML, PDF, etc.).

# Example 8: Additional Considerations
# - Use descriptive names for parameters and return values.
# - Include examples and usage scenarios in docstrings.

# Note: The examples above show basic docstrings. Sphinx allows more extensive documentation.

# Additional Resources:
# - Sphinx Documentation: https://www.sphinx-doc.org/en/master/

# Example 9: Function with Examples
def power(base, exponent):
    """
    Calculate the power of a number.

    :param float base: The base number.
    :param int exponent: The exponent.

    :return: The result of the power operation.
    :rtype: float

    :Example:
    
    >>> power(2, 3)
    8.0
    
    >>> power(3, 2)
    9.0
    """
    return base ** exponent


# --------------------
# OUTPUT
# --------------------

# No output as this script focuses on documenting functions.

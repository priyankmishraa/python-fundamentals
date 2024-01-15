# Script: Modules in Python

# Explanation: Modules
# A module is a file containing Python definitions and statements. It allows code organization and reuse.

# Example 1: Creating a Simple Module
# Save this code in a file named "math_operations.py"

# math_operations.py
def add(a, b):
    """Function to add two numbers."""
    return a + b

def subtract(a, b):
    """Function to subtract two numbers."""
    return a - b

def multiply(a, b):
    """Function to multiply two numbers."""
    return a * b

def divide(a, b):
    """Function to divide two numbers."""
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

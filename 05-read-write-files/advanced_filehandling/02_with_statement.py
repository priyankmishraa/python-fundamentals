# Script: Context Managers and Options in Python

# Explanation: Context Managers
# Context managers in Python provide a way to manage resources efficiently using the 'with' statement.

# Example 1: Using the 'with' Statement with File Handling
def read_file_with_context(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError as e:
        return f"Error: {e}"

# Uncomment the line below to see the behavior of the file handling example
# file_content = read_file_with_context("example.txt")

# Example 2: Creating a Custom Context Manager Class
class CustomContextManager:
    def __enter__(self):
        print("Entering the context")
        return self  # Can return any object to be used within the 'with' block

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

# Using the custom context manager
# with CustomContextManager() as context:
#     print("Inside the context")

# Example 3: Using the 'contextlib' Module for Creating a Context Manager
from contextlib import contextmanager

@contextmanager
def custom_context_manager():
    print("Entering the context")
    yield  # The point where the 'with' block gets executed
    print("Exiting the context")

# Using the context manager created with 'contextlib'
# with custom_context_manager():
#     print("Inside the context")

# Example 4: Handling Exceptions with Context Managers
def handle_exceptions_with_context(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            # Simulating an exception
            int(content)  # This line will raise a ValueError
        return content
    except FileNotFoundError as e:
        return f"Error: {e}"
    except ValueError as e:
        return f"Error: {e}"

# Uncomment the line below to see the behavior of handling exceptions with context
# file_content_with_exception = handle_exceptions_with_context("example.txt")

# -----------------------
# OUTPUT
# -----------------------

# Entering the context
# Inside the context
# Exiting the context

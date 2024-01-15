# Script: Local to Global Scope in Python Functions

# Explanation: Local and Global Scope
# Variables declared inside a function have local scope, while those declared outside have global scope.

# Example 1: Local Variable
def example_function():
    # Local variable
    local_variable = "I am local"
    print(local_variable)

# Call the function
example_function()

# Uncomment the line below to see the NameError
# print(local_variable)

# Example 2: Local Scope Example with Parameters
def calculate_sum(a, b):
    # Local variables a and b
    result = a + b
    return result

# Call the function
sum_result = calculate_sum(3, 4)
print("Sum:", sum_result)

# Uncomment the line below to see the NameError
# print(result)

# Example 3: Global Variable
global_variable = "I am global"

def print_global():
    # Accessing global variable
    print(global_variable)

# Call the function
print_global()

# Example 4: Modifying Global Variable within Function
counter = 0

def increment_counter():
    # Modifying global variable
    global counter
    counter += 1
    print("Counter:", counter)

# Call the function
increment_counter()
increment_counter()

# Example 5: Local vs Global Scope Lifecycle
def lifecycle_example():
    local_variable = "Local variable"

    def nested_function():
        # Accessing local variable from enclosing scope
        print("Nested Function:", local_variable)

    # Call the nested function
    nested_function()

    # Accessing local variable within the outer function
    print("Outer Function:", local_variable)

# Call the function
lifecycle_example()

# Uncomment the line below to see the NameError
# print(local_variable)

# Example 6: Avoiding Global Variables (Best Practice)
def avoid_global():
    # Avoid using global variables when not necessary
    local_result = 42
    return local_result

# Call the function
result = avoid_global()
print("Result:", result)


# --------------------
# OUTPUT
# --------------------

# I am local
# Sum: 7
# I am global
# Counter: 1
# Counter: 2
# Nested Function: Local variable
# Outer Function: Local variable
# Result: 42

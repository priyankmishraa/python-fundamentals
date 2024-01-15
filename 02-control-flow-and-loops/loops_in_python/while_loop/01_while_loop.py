# Script: While Loop in Python

# Explanation: While Loop
# The while loop is used to repeatedly execute a block of code as long as a certain condition is true.

# Example 1: Simple While Loop
count = 1
print("Simple While Loop:")
while count <= 5:
    print(count, end=' ')
    count += 1
print()

# Example 2: While Loop with User Input
print("\nWhile Loop with User Input:")
user_input = input("Enter 'stop' to exit: ")
while user_input.lower() != 'stop':
    print(f"You entered: {user_input}")
    user_input = input("Enter 'stop' to exit: ")

# Example 3: While Loop with Break Statement
print("\nWhile Loop with Break Statement:")
while True:
    password = input("Enter the password: ")
    if password == 'secret':
        print("Access granted!")
        break
    else:
        print("Incorrect password. Try again.")

# Example 4: While Loop with Continue Statement
print("\nWhile Loop with Continue Statement:")
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print(num, end=' ')



# --------------------
# OUTPUT
# --------------------
    
# Simple While Loop:
# 1 2 3 4 5

# While Loop with User Input:
# Enter 'stop' to exit: hello
# You entered: hello
# Enter 'stop' to exit: world
# You entered: world
# Enter 'stop' to exit: stop

# While Loop with Break Statement:
# Enter the password: pass
# Incorrect password. Try again.
# Enter the password: secret
# Access granted!

# While Loop with Continue Statement:
# 1 2 4 5 

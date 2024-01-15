# Script: Introduction to the `if` Statement in Python

# Explanation: if Statement
# The `if` statement is used to check a condition, and if the condition is true, it executes a block of code.

# Example 1:
temperature = 25

if temperature > 30:
    print("It's a hot day.")
    print("Stay hydrated.")

# Example 2:
age = 18

if age >= 18:
    print("You are eligible to vote.")
    print("Make your voice heard!")

# Example 3: Using the `else` Statement
mark = 75

if mark >= 60:
    print("Congratulations! You passed.")
else:
    print("Sorry, you did not pass.")

# Example 4: Using the `elif` Statement
score = 85

if score >= 90:
    print("You got an A.")
elif score >= 80:
    print("You got a B.")
elif score >= 70:
    print("You got a C.")
else:
    print("You need improvement.")



# --------------------
# OUTPUT
# --------------------
    
# It's a hot day.
# Stay hydrated.
# You are eligible to vote.
# Make your voice heard!
# Congratulations! You passed.
# You got a B.

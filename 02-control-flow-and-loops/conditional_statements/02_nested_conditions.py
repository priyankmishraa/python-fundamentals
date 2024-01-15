# Script: Nested Conditional Statements in Python

# Explanation: Nested If Statements
# Nested if statements involve placing one if statement inside another.

# Example 1:
temperature = 28
humidity = 60

if temperature > 30:
    print("It's a hot day.")
    if humidity > 50:
        print("And it's humid too.")
    else:
        print("It's not too humid.")

# Example 2:
grade = 85

if grade >= 80:
    print("You passed.")
    if grade >= 90:
        print("With distinction.")
    elif grade >= 85:
        print("Well done.")
    else:
        print("Good job.")
else:
    print("You did not pass.")

# Example 3: Complex Nesting
x = 5
y = 10

if x > 0:
    print("x is positive.")
    if y > 0:
        print("y is also positive.")
        if x > y:
            print("x is greater than y.")
        else:
            print("y is greater than or equal to x.")
    else:
        print("y is non-positive.")
else:
    print("x is non-positive.")



# --------------------
# OUTPUT
# --------------------
    
# It's a hot day.
# And it's humid too.
# You passed.
# Well done.
# x is positive.
# y is also positive.
# y is greater than or equal to x.

# Script: Break and Continue in Python with While Loop

# Explanation: Break and Continue in While Loop
# The break statement is used to exit a loop prematurely, and the continue statement is used to skip the rest of the code in the current iteration.

# Example 1: Using Break to Exit Loop
print("Using Break to Exit Loop:")
count = 1
while count <= 10:
    print(count, end=' ')
    if count == 5:
        break
    count += 1
print("\nLoop ended with break.")

# Example 2: Using Continue to Skip Iteration
print("\nUsing Continue to Skip Iteration:")
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print(num, end=' ')
print("\nLoop ended with continue.")



# --------------------
# OUTPUT
# --------------------

# Using Break to Exit Loop:
# 1 2 3 4 5 
# Loop ended with break.

# Using Continue to Skip Iteration:
# 1 2 4 5 
# Loop ended with continue.

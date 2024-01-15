# Script: Range Function and Its Features

# Explanation: Range Function
# The range() function is used to generate a sequence of numbers.

# Example 1: Using range() with Stop
print("Using range() with stop:")
for number in range(5):
    print(number)

# Example 2: Using range() with Start and Stop
print("\nUsing range() with start and stop:")
for number in range(2, 7):
    print(number)

# Example 3: Using range() with Start, Stop, and Step
print("\nUsing range() with start, stop, and step:")
for number in range(1, 10, 2):
    print(number)

# Example 4: Creating a List from range()
numbers_list = list(range(3, 12, 3))
print("\nCreating a list from range():", numbers_list)

# Example 5: Using range() in Reverse
print("\nUsing range() in reverse:")
for number in range(10, 5, -1):
    print(number)

# Example 6: Checking if a Value is in a Range
value_to_check = 7
is_in_range = value_to_check in range(5, 10)
print("\nIs", value_to_check, "in the range (5, 10)?", is_in_range)



# --------------------
# OUTPUT
# --------------------

# Using range() with stop:
# 0
# 1
# 2
# 3
# 4

# Using range() with start and stop:
# 2
# 3
# 4
# 5
# 6

# Using range() with start, stop, and step:
# 1
# 3
# 5
# 7
# 9

# Creating a list from range(): [3, 6, 9]

# Using range() in reverse:
# 10
# 9
# 8
# 7
# 6

# Is 7 in the range (5, 10)? True


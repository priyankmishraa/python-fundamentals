# Script: Iterating Through Sequences Using For Loops

# Explanation: Iterating Through Sequences
# For loops can be used to iterate through sequences such as lists, tuples, and strings.

# Example 1: Iterating through a List
fruits = ['apple', 'banana', 'cherry']
print("Iterating through a list:")
for fruit in fruits:
    print(fruit)

# Example 2: Iterating through a Tuple
colors = ('red', 'green', 'blue')
print("\nIterating through a tuple:")
for color in colors:
    print(color)

# Example 3: Iterating through a String
word = 'Python'
print("\nIterating through a string:")
for char in word:
    print(char)

# Example 4: Using enumerate() for Index and Value
grades = ['A', 'B', 'C']
print("\nUsing enumerate() for index and value:")
for index, grade in enumerate(grades):
    print(f"Index: {index}, Grade: {grade}")

# Example 5: Iterating through a Range
print("\nIterating through a range:")
for number in range(3, 8):
    print(number)



# --------------------
# OUTPUT
# --------------------

# Iterating through a list:
# apple
# banana
# cherry

# Iterating through a tuple:
# red
# green
# blue

# Iterating through a string:
# P
# y
# t
# h
# o
# n

# Using enumerate() for index and value:
# Index: 0, Grade: A
# Index: 1, Grade: B
# Index: 2, Grade: C

# Iterating through a range:
# 3
# 4
# 5
# 6
# 7

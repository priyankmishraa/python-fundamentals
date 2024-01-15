# Script: For Loops in Python

# Explanation: For Loops
# For loops in Python are used for iterating over a sequence.

# Example 1: Iterating over a List
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Example 2: Iterating over a Tuple
colors = ('red', 'green', 'blue')
for color in colors:
    print(color)

# Example 3: Iterating over a String
word = 'Python'
for char in word:
    print(char)

# Example 4: Iterating with Range
for number in range(5):
    print(number)

# Example 5: Using range() with Start and Step
for even_number in range(2, 10, 2):
    print(even_number)

# Example 6: Iterating over Dictionary Keys
student = {'name': 'John', 'age': 20, 'grade': 'B'}
for key in student:
    print(key)

# Example 7: Iterating over Dictionary Items
for key, value in student.items():
    print(f"{key}: {value}")



# --------------------
# OUTPUT
# --------------------

# apple
# banana
# cherry
# red
# green
# blue
# P
# y
# t
# h
# o
# n
# 0
# 1
# 2
# 3
# 4
# 2
# 4
# 6
# 8
# name
# age
# grade
# name: John
# age: 20
# grade: B

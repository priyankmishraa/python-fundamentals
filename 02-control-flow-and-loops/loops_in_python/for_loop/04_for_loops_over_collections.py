# Script: For Loops Over Collections

# Explanation: For Loops over Collections
# For loops can be used to iterate over elements in collections such as lists, tuples, and dictionaries.

# Example 1: For Loop over a List
fruits = ['apple', 'banana', 'cherry']
print("For loop over a list:")
for fruit in fruits:
    print(fruit)

# Example 2: For Loop over a Tuple
colors = ('red', 'green', 'blue')
print("\nFor loop over a tuple:")
for color in colors:
    print(color)

# Example 3: For Loop over a String
word = 'Python'
print("\nFor loop over a string:")
for char in word:
    print(char)

# Example 4: For Loop over a Dictionary (Keys)
student = {'name': 'John', 'age': 20, 'grade': 'B'}
print("\nFor loop over dictionary keys:")
for key in student:
    print(key)

# Example 5: For Loop over a Dictionary (Items)
print("\nFor loop over dictionary items:")
for key, value in student.items():
    print(f"{key}: {value}")

# Example 6: Using enumerate() for Index and Value
grades = ['A', 'B', 'C']
print("\nUsing enumerate() for index and value:")
for index, grade in enumerate(grades):
    print(f"Index: {index}, Grade: {grade}")



# --------------------
# OUTPUT
# --------------------

# For loop over a list:
# apple
# banana
# cherry

# For loop over a tuple:
# red
# green
# blue

# For loop over a string:
# P
# y
# t
# h
# o
# n

# For loop over dictionary keys:
# name
# age
# grade

# For loop over dictionary items:
# name: John
# age: 20
# grade: B

# Using enumerate() for index and value:
# Index: 0, Grade: A
# Index: 1, Grade: B
# Index: 2, Grade: C

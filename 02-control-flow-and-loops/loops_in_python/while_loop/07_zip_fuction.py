# Script: Using Zip Function with Different Collections

# Explanation: Zip Function
# The zip() function is used to combine elements from multiple iterables into tuples.

# Example 1: Using Zip with Lists
fruits = ['apple', 'banana', 'cherry']
colors = ['red', 'yellow', 'pink']
print("Using Zip with Lists:")
zipped_lists = zip(fruits, colors)
for fruit, color in zipped_lists:
    print(f"Fruit: {fruit}, Color: {color}")

# Example 2: Using Zip with Tuples
numbers = (1, 2, 3)
letters = ('a', 'b', 'c')
print("\nUsing Zip with Tuples:")
zipped_tuples = zip(numbers, letters)
for number, letter in zipped_tuples:
    print(f"Number: {number}, Letter: {letter}")

# Example 3: Using Zip with Strings
word = 'Python'
numbers = [1, 2, 3, 4, 5]
print("\nUsing Zip with String and List:")
zipped_string_list = zip(word, numbers)
for char, num in zipped_string_list:
    print(f"Char: {char}, Number: {num}")

# Example 4: Using Zip with Sets
set1 = {1, 2, 3}
set2 = {'a', 'b', 'c'}
print("\nUsing Zip with Sets:")
zipped_sets = zip(set1, set2)
for element1, element2 in zipped_sets:
    print(f"Element from Set 1: {element1}, Element from Set 2: {element2}")

# Example 5: Using Zip with Lists of Different Lengths
list1 = ['apple', 'banana', 'cherry']
list2 = ['red', 'yellow']
print("\nUsing Zip with Lists of Different Lengths:")
zipped_lists_diff_lengths = zip(list1, list2)
for item1, item2 in zipped_lists_diff_lengths:
    print(f"Item from List 1: {item1}, Item from List 2: {item2}")



# --------------------
# OUTPUT
# --------------------

# Using Zip with Lists:
# Fruit: apple, Color: red
# Fruit: banana, Color: yellow
# Fruit: cherry, Color: pink

# Using Zip with Tuples:
# Number: 1, Letter: a
# Number: 2, Letter: b
# Number: 3, Letter: c

# Using Zip with String and List:
# Char: P, Number: 1
# Char: y, Number: 2
# Char: t, Number: 3
# Char: h, Number: 4
# Char: o, Number: 5

# Using Zip with Sets:
# Element from Set 1: 1, Element from Set 2: a
# Element from Set 1: 2, Element from Set 2: b
# Element from Set 1: 3, Element from Set 2: c

# Using Zip with Lists of Different Lengths:
# Item from List 1: apple, Item from List 2: red
# Item from List 1: banana, Item from List 2: yellow

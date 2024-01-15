# Script: Lists in Python

# Explanation: Lists
# Lists are a versatile and widely used data structure in Python to store an ordered collection of items.

# Example 1: Creating a List
fruits = ['apple', 'banana', 'cherry', 'date']
print("List of fruits:", fruits)

# Example 2: Accessing Elements
first_fruit = fruits[0]
print("First fruit:", first_fruit)

# Example 3: Modifying Elements
fruits[1] = 'orange'
print("Updated list:", fruits)

# Example 4: Adding Elements
fruits.append('grape')
print("List after adding 'grape':", fruits)

# Example 5: Removing Elements
removed_fruit = fruits.pop(2)
print("Removed fruit:", removed_fruit)
print("List after removing element at index 2:", fruits)

# Example 6: Slicing
selected_fruits = fruits[1:4]
print("Selected fruits using slicing:", selected_fruits)

# Example 7: Checking Membership
is_banana_in_list = 'banana' in fruits
print("Is 'banana' in the list?", is_banana_in_list)

# Example 8: Length of List
list_length = len(fruits)
print("Length of the list:", list_length)

# Example 9: List Concatenation
more_fruits = ['kiwi', 'melon']
all_fruits = fruits + more_fruits
print("Combined list of fruits:", all_fruits)


# --------------------
# OUTPUT
# --------------------

# List of fruits: ['apple', 'banana', 'cherry', 'date']
# First fruit: apple
# Updated list: ['apple', 'orange', 'cherry', 'date']
# List after adding 'grape': ['apple', 'orange', 'cherry', 'date', 'grape']
# Removed fruit: cherry
# List after removing element at index 2: ['apple', 'orange', 'date', 'grape']
# Selected fruits using slicing: ['orange', 'date', 'grape']
# Is 'banana' in the list? False
# Length of the list: 4
# Combined list of fruits: ['apple', 'orange', 'date', 'grape', 'kiwi', 'melon']

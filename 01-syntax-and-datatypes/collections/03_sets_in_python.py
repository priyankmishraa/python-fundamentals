# Script: Sets in Python

# Explanation: Sets
# Sets are unordered collections of unique elements.

# Example 1: Creating a Set
fruits_set = {'apple', 'banana', 'cherry'}
print("Set of fruits:", fruits_set)

# Example 2: Adding Elements to a Set
fruits_set.add('orange')
print("Set after adding 'orange':", fruits_set)

# Example 3: Removing Elements from a Set
fruits_set.remove('banana')
print("Set after removing 'banana':", fruits_set)

# Example 4: Set Operations
vegetables_set = {'carrot', 'spinach', 'tomato'}

# Union of sets
union_set = fruits_set.union(vegetables_set)
print("Union of sets:", union_set)

# Intersection of sets
intersection_set = fruits_set.intersection(vegetables_set)
print("Intersection of sets:", intersection_set)

# Difference of sets
difference_set = fruits_set.difference(vegetables_set)
print("Difference of sets:", difference_set)

# Example 5: Checking Membership
is_apple_in_set = 'apple' in fruits_set
print("Is 'apple' in the set?", is_apple_in_set)

# Example 6: Length of Set
set_length = len(fruits_set)
print("Length of the set:", set_length)



# --------------------
# OUTPUT
# --------------------

# Set of fruits: {'cherry', 'banana', 'apple'}
# Set after adding 'orange': {'cherry', 'banana', 'apple', 'orange'}
# Set after removing 'banana': {'cherry', 'apple', 'orange'}
# Union of sets: {'carrot', 'spinach', 'tomato', 'cherry', 'apple', 'orange'}
# Intersection of sets: {'apple', 'orange'}
# Difference of sets: {'cherry'}
# Is 'apple' in the set? True
# Length of the set: 3

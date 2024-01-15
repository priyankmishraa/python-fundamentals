# Script: Dictionaries in Python

# Explanation: Dictionaries
# Dictionaries are unordered collections of key-value pairs.

# Example 1: Creating a Dictionary
student = {'name': 'John', 'age': 20, 'grade': 'B'}
print("Dictionary of student:", student)

# Example 2: Accessing Elements by Key
student_name = student['name']
print("Student's name:", student_name)

# Example 3: Modifying Values
student['age'] = 21
print("Updated dictionary:", student)

# Example 4: Adding a New Key-Value Pair
student['city'] = 'New York'
print("Dictionary after adding 'city':", student)

# Example 5: Removing a Key-Value Pair
removed_grade = student.pop('grade')
print("Removed grade:", removed_grade)
print("Dictionary after removing 'grade':", student)

# Example 6: Checking if a Key Exists
has_age_key = 'age' in student
print("Does 'age' key exist?", has_age_key)

# Example 7: Getting All Keys and Values
all_keys = student.keys()
all_values = student.values()
print("All keys:", all_keys)
print("All values:", all_values)

# Example 8: Length of Dictionary
dictionary_length = len(student)
print("Length of the dictionary:", dictionary_length)


# --------------------
# OUTPUT
# --------------------

# Dictionary of student: {'name': 'John', 'age': 20, 'grade': 'B'}
# Student's name: John
# Updated dictionary: {'name': 'John', 'age': 21, 'grade': 'B'}
# Dictionary after adding 'city': {'name': 'John', 'age': 21, 'grade': 'B', 'city': 'New York'}
# Removed grade: B
# Dictionary after removing 'grade': {'name': 'John', 'age': 21, 'city': 'New York'}
# Does 'age' key exist? True
# All keys: dict_keys(['name', 'age', 'city'])
# All values: dict_values(['John', 21, 'New York'])
# Length of the dictionary: 3

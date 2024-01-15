# Script: Access Index and Value Without Enumerate Function

# Explanation: Access Index and Value Without Enumerate
# You can manually track the index while iterating over the elements to achieve similar functionality to the enumerate() function.

# Example 1: Accessing Index and Value of a List
fruits = ['apple', 'banana', 'cherry']
print("Accessing Index and Value of a List:")
for index in range(len(fruits)):
    value = fruits[index]
    print(f"Index: {index}, Value: {value}")

# Example 2: Accessing Index and Value of a Tuple
colors = ('red', 'green', 'blue')
print("\nAccessing Index and Value of a Tuple:")
for index in range(len(colors)):
    value = colors[index]
    print(f"Index: {index}, Value: {value}")

# Example 3: Accessing Index and Value of a String
word = 'Python'
print("\nAccessing Index and Value of a String:")
for index in range(len(word)):
    char = word[index]
    print(f"Index: {index}, Char: {char}")

# Example 4: Accessing Index and Value of a Dictionary (Keys and Values)
student = {'name': 'John', 'age': 20, 'grade': 'B'}
print("\nAccessing Index and Value of a Dictionary (Keys and Values):")
keys = list(student.keys())
values = list(student.values())
for index in range(len(keys)):
    key = keys[index]
    value = values[index]
    print(f"Key: {key}, Value: {value}")



# --------------------
# OUTPUT
# --------------------
    
# Accessing Index and Value of a List:
# Index: 0, Value: apple
# Index: 1, Value: banana
# Index: 2, Value: cherry

# Accessing Index and Value of a Tuple:
# Index: 0, Value: red
# Index: 1, Value: green
# Index: 2, Value: blue

# Accessing Index and Value of a String:
# Index: 0, Char: P
# Index: 1, Char: y
# Index: 2, Char: t
# Index: 3, Char: h
# Index: 4, Char: o
# Index: 5, Char: n

# Accessing Index and Value of a Dictionary (Keys and Values):
# Key: name, Value: John
# Key: age, Value: 20
# Key: grade, Value: B

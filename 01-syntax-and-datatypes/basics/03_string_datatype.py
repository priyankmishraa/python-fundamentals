# Script: Mastering String Data Types in Python

# Explanation: Creating Strings
# Strings are created by enclosing text in single (''), double (" "), or triple (''' or """) quotes.

# Example 1: Creating Strings
single_quoted_string = 'Hello, Python!'
double_quoted_string = "Python is fun!"
triple_quoted_string = '''This is a multiline string
that spans multiple lines.'''

print("Single Quoted String:", single_quoted_string)
print("Double Quoted String:", double_quoted_string)
print("Triple Quoted String:")
print(triple_quoted_string)

# Explanation: String Concatenation
# Concatenate (combine) strings using the '+' operator.

# Example 2: String Concatenation
first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name
print("Full Name:", full_name)

# Explanation: String Methods
# Strings have various built-in methods for manipulation.

# Example 3: String Methods
sentence = "Python is an amazing programming language."

# Convert to uppercase
uppercase_sentence = sentence.upper()
print("Uppercase Sentence:", uppercase_sentence)

# Find the index of a substring
index_of_amazing = sentence.find("amazing")
print("Index of 'amazing':", index_of_amazing)

# Replace a substring
new_sentence = sentence.replace("Python", "Java")
print("New Sentence:", new_sentence)

# Explanation: String Formatting
# Use f-strings or the format() method for string formatting.

# Example 4: String Formatting
age = 25
formatted_string = f"My age is {age}."
print(formatted_string)

# Example 5: String Formatting using format() method
greeting = "Hello, {}!"
formatted_greeting = greeting.format("World")
print(formatted_greeting)


# --------------------
# OUTPUT
# --------------------

# Single Quoted String: Hello, Python!
# Double Quoted String: Python is fun!
# Triple Quoted String:
# This is a multiline string
# that spans multiple lines.
# Full Name: John Doe
# Uppercase Sentence: PYTHON IS AN AMAZING PROGRAMMING LANGUAGE.
# Index of 'amazing': 18
# New Sentence: Java is an amazing programming language.
# My age is 25.
# Hello, World!

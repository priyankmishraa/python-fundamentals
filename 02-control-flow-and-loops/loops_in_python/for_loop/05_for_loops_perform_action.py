# Script: For Loops to Perform Actions

# Explanation: For Loops to Perform Actions
# For loops can be used to iterate over collections and perform specific actions on each iteration.

# Example 1: Calculating Squares of Numbers
numbers = [1, 2, 3, 4, 5]
squares = []
print("Calculating squares of numbers:")
for number in numbers:
    square = number ** 2
    squares.append(square)
print("Squares:", squares)

# Example 2: Filtering Even Numbers
numbers = [10, 21, 34, 45, 50]
even_numbers = []
print("\nFiltering even numbers:")
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print("Even Numbers:", even_numbers)

# Example 3: Reversing Strings
words = ['apple', 'banana', 'cherry']
reversed_words = []
print("\nReversing strings:")
for word in words:
    reversed_word = word[::-1]
    reversed_words.append(reversed_word)
print("Reversed Words:", reversed_words)

# Example 4: Counting Vowels in Strings
sentences = ['Hello, World!', 'Python is fun.']
vowel_counts = []
print("\nCounting vowels in strings:")
for sentence in sentences:
    vowel_count = sum(1 for char in sentence if char.lower() in 'aeiou')
    vowel_counts.append(vowel_count)
print("Vowel Counts:", vowel_counts)



# --------------------
# OUTPUT
# --------------------

# Calculating squares of numbers:
# Squares: [1, 4, 9, 16, 25]

# Filtering even numbers:
# Even Numbers: [10, 34, 50]

# Reversing strings:
# Reversed Words: ['elppa', 'ananab', 'yrrehc']

# Counting vowels in strings:
# Vowel Counts: [3, 5]

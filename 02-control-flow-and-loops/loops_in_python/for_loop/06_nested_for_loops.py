# Script: Nested For Loops

# Explanation: Nested For Loops
# Nested for loops allow multiple levels of iteration, useful for working with nested data structures.

# Example 1: Nested Loop to Print Patterns
print("Nested Loop to Print Patterns:")
for i in range(4):
    for j in range(i + 1):
        print('*', end=' ')
    print()

# Example 2: Nested Loop for Matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nNested Loop for Matrix:")
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()

# Example 3: Nested Loop for Multiplication Table
print("\nNested Loop for Multiplication Table:")
for i in range(1, 6):
    for j in range(1, 6):
        product = i * j
        print(f"{i} x {j} = {product}", end='\t')
    print()

# Example 4: Nested Loop to Find Prime Numbers
print("\nNested Loop to Find Prime Numbers:")
for num in range(2, 20):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')

# Example 5: Nested Loop for Combinations
colors = ['red', 'green', 'blue']
print("\n\nNested Loop for Combinations:")
for color1 in colors:
    for color2 in colors:
        if color1 != color2:
            print(f"{color1} and {color2}")




# --------------------
# OUTPUT
# --------------------

# Nested Loop to Print Patterns:
# * 
# * * 
# * * * 
# * * * * 

# Nested Loop for Matrix:
# 1 2 3 
# 4 5 6 
# 7 8 9 

# Nested Loop for Multiplication Table:
# 1 x 1 = 1	1 x 2 = 2	1 x 3 = 3	1 x 4 = 4	1 x 5 = 5	
# 2 x 1 = 2	2 x 2 = 4	2 x 3 = 6	2 x 4 = 8	2 x 5 = 10	
# 3 x 1 = 3	3 x 2 = 6	3 x 3 = 9	3 x 4 = 12	3 x 5 = 15	
# 4 x 1 = 4	4 x 2 = 8	4 x 3 = 12	4 x 4 = 16	4 x 5 = 20	
# 5 x 1 = 5	5 x 2 = 10	5 x 3 = 15	5 x 4 = 20	5 x 5 = 25	

# Nested Loop to Find Prime Numbers:
# 2 3 5 7 11 13 17 19 

# Nested Loop for Combinations:
# red and green
# red and blue
# green and red
# green and blue
# blue and red
# blue and green

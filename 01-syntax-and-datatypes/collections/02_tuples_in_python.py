# Script: Tuples in Python

# Explanation: Tuples
# Tuples are ordered collections of items, similar to lists, but they are immutable.

# Example 1: Creating a Tuple
colors = ('red', 'green', 'blue')
print("Tuple of colors:", colors)

# Example 2: Accessing Elements
first_color = colors[0]
print("First color:", first_color)

# Example 3: Trying to Modify a Tuple (This will raise an error)
try:
    colors[1] = 'yellow'
except TypeError as e:
    print("Error:", e)

# Example 4: Tuple Unpacking
x, y, z = colors
print("Unpacked values:", x, y, z)

# Example 5: Length of Tuple
tuple_length = len(colors)
print("Length of the tuple:", tuple_length)

# Example 6: Checking Membership
is_green_in_tuple = 'green' in colors
print("Is 'green' in the tuple?", is_green_in_tuple)

# Example 7: Concatenating Tuples
more_colors = ('yellow', 'purple')
all_colors = colors + more_colors
print("Combined tuple of colors:", all_colors)


# --------------------
# OUTPUT
# --------------------

# Tuple of colors: ('red', 'green', 'blue')
# First color: red
# Error: 'tuple' object does not support item assignment
# Unpacked values: red green blue
# Length of the tuple: 3
# Is 'green' in the tuple? True
# Combined tuple of colors: ('red', 'green', 'blue', 'yellow', 'purple')

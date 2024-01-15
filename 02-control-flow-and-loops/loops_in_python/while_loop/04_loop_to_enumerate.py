# Script: Looping to Enumerate without Enumerate Function

# Explanation: Looping to Enumerate
# You can manually track the index while iterating over elements to achieve similar functionality to the enumerate() function.

# Example: Looping to Enumerate without Enumerate Function
fruits = ['apple', 'banana', 'cherry']

# Using a for loop with a range and len() to manually track the index
print("Using a for loop to enumerate:")
for i in range(len(fruits)):
    print(f"Index: {i}, Fruit: {fruits[i]}")

# Using a while loop to achieve the same result
print("\nUsing a while loop to enumerate:")
index = 0
while index < len(fruits):
    print(f"Index: {index}, Fruit: {fruits[index]}")
    index += 1



# --------------------
# OUTPUT
# --------------------
    
# Using a for loop to enumerate:
# Index: 0, Fruit: apple
# Index: 1, Fruit: banana
# Index: 2, Fruit: cherry

# Using a while loop to enumerate:
# Index: 0, Fruit: apple
# Index: 1, Fruit: banana
# Index: 2, Fruit: cherry

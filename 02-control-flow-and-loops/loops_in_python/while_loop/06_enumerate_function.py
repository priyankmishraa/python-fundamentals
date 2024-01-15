
# Script: Infinite Loops and Practical Uses

# Explanation: Infinite Loops
# An infinite loop is a loop that runs indefinitely without a specific exit condition.

# Example 1: Simple Infinite Loop
print("Example of a Simple Infinite Loop:")
while True:
    print("This is an infinite loop. Press Ctrl+C to exit.")

# Example 2: Practical Use - Interactive Menu
print("\nPractical Use - Interactive Menu:")
while True:
    print("\nChoose an option:")
    print("1. Perform Task 1")
    print("2. Perform Task 2")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("Task 1 is performed.")
    elif choice == '2':
        print("Task 2 is performed.")
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

# Example 3: Practical Use - Monitoring System
print("\nPractical Use - Monitoring System:")
import time

while True:
    # Simulating a monitoring task
    print("Monitoring system is active. Press Ctrl+C to stop.")
    time.sleep(5)  # Sleep for 5 seconds before the next iteration


# --------------------
# OUTPUT
# --------------------

# Example of a Simple Infinite Loop:
# This is an infinite loop. Press Ctrl+C to exit.

# Practical Use - Interactive Menu:

# Choose an option:
# 1. Perform Task 1
# 2. Perform Task 2
# 3. Exit
# Enter your choice: 1
# Task 1 is performed.

# Choose an option:
# 1. Perform Task 1
# 2. Perform Task 2
# 3. Exit
# Enter your choice: 2
# Task 2 is performed.

# Choose an option:
# 1. Perform Task 1
# 2. Perform Task 2
# 3. Exit
# Enter your choice: 3
# Exiting the program.

# Practical Use - Monitoring System:
# Monitoring system is active. Press Ctrl+C to stop.
# Monitoring system is active. Press Ctrl+C to stop.
# Monitoring system is active. Press Ctrl+C to stop.
# ...

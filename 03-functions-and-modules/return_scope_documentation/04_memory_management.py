# Script: Memory Management and Garbage Collection in Python

# Explanation: Memory Management
# Memory management involves allocating and deallocating memory during the execution of a program.

# Example 1: Memory Allocation
def allocate_memory():
    # Creating objects that allocate memory
    list_object = [1, 2, 3, 4, 5]
    string_object = "Hello, Python!"
    tuple_object = (10, 20, 30)

    # Accessing objects
    print(list_object)
    print(string_object)
    print(tuple_object)

# Call the function
allocate_memory()

# Example 2: Garbage Collection
# Python uses a garbage collector to automatically reclaim memory occupied by objects that are no longer in use.

# Example 3: Circular Reference (Potential Memory Leak)
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

# Creating circular reference (potential memory leak)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next_node = node2
node2.next_node = node3
node3.next_node = node1

# Breaking the circular reference
node1.next_node = None
node2.next_node = None
node3.next_node = None

# Example 4: Manual Memory Management (Not Recommended)
# Python's garbage collector handles memory automatically, and manual management is generally not needed.
# However, understanding the concepts is valuable.

import gc

def manual_memory_management():
    # Creating objects
    obj1 = [1, 2, 3]
    obj2 = "Python"
    obj3 = (4, 5, 6)

    # Deleting objects manually (not recommended)
    del obj1
    del obj2
    del obj3

    # Collecting garbage manually
    gc.collect()

# Uncomment the lines below to see the impact on memory
# manual_memory_management()

# Example 5: Memory Usage Monitoring (Using psutil)
# Install psutil using: pip install psutil

import psutil

def memory_usage():
    # Function to check memory usage
    process = psutil.Process()
    memory_info = process.memory_info()

    print("Memory Usage:")
    print(f"RSS (Resident Set Size): {memory_info.rss / (1024 * 1024):.2f} MB")
    print(f"VMS (Virtual Memory Size): {memory_info.vms / (1024 * 1024):.2f} MB")

# Call the function to check memory usage
memory_usage()


# --------------------
# OUTPUT
# --------------------

# [1, 2, 3, 4, 5]
# Hello, Python!
# (10, 20, 30)
# Memory Usage:
# RSS (Resident Set Size): 27.19 MB
# VMS (Virtual Memory Size): 155.81 MB

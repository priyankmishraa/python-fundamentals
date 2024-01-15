# Script: Using the __name__ == "__main__": Block

# Explanation: __name__ == "__main__": Block
# This block is executed only if the script is run as the main program and not when imported as a module.

# Example 1: Script with __name__ == "__main__": Block
# Save this code in a file named "main_execution.py"

# main_execution.py
import math_operations

def main():
    # Using functions from the module
    result_add = math_operations.add(5, 3)
    result_multiply = math_operations.multiply(2, 6)

    # Displaying results
    print("Addition:", result_add)
    print("Multiplication:", result_multiply)

if __name__ == "__main__":
    # Execute main() only if the script is run as the main program
    main()

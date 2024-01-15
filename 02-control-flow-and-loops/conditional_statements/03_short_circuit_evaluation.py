# Script: Short-Circuit Evaluation in Python

# Explanation: Short-Circuit Evaluation
# Short-circuit evaluation is a feature where the interpreter does not evaluate the entire boolean expression
# if the result can be determined from part of it.

# Example 1: Short-Circuit with `and` Operator
x = 5

if x > 0 and (10 / x) > 2:
    print("Both conditions are true.")
else:
    print("Short-circuit occurred.")

# Example 2: Short-Circuit with `or` Operator
y = 0

if y == 0 or (10 / y) > 2:
    print("At least one condition is true.")
else:
    print("Short-circuit occurred.")



# --------------------
# OUTPUT
# --------------------
    
# Both conditions are true.
# Short-circuit occurred.

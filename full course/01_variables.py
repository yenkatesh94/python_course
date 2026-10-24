"""Variables give names to values so a program can reuse them.
This example introduces common Python types: text, integers, decimals, and booleans.
"""

# Topic 1: Variables and data types
# Variables store information that a program can use.
# Use = to give a variable a value.

student_name = "Maya"  # str: text
student_age = 12        # int: whole number
height_in_meters = 1.5  # float: decimal number
is_learning_python = True  # bool: True or False

# Display the values. An f-string inserts each variable into the message.
print(f"Name: {student_name}")
print(f"Age: {student_age}")
print(f"Height: {height_in_meters} meters")
print(f"Learning Python: {is_learning_python}")

# Variables can be updated by assigning a new value.
student_age = student_age + 1
print(f"Next year, {student_name} will be {student_age}.")
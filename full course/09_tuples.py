"""Tuples are ordered collections that cannot be changed after creation.
This example shows indexing, slicing, tuple methods, unpacking, and safe rebuilding.
"""

# Tuples are immutable ordered collections

numbers = (10, 20, 30, 10)
print(numbers)
print(type(numbers))
print(len(numbers))

# Accessing elements
print(numbers[0])
print(numbers[-1])
print(numbers[1:3])

# Tuples have two built-in methods:
# count(value) returns how many times a value appears.
print("Number of 10s:", numbers.count(10))

# index(value) returns the position of the first matching value.
print("First 30 is at index:", numbers.index(30))

# index(value, start, stop) can search only part of the tuple.
print("10 found from index 1 onward:", numbers.index(10, 1))

# Tuple unpacking
student = ("Alice", 21, "CS")
name, age, dept = student
print(name, age, dept)

# Tuples cannot be modified after creation
# numbers[0] = 99  # This will raise TypeError
# Topic 9: Tuples

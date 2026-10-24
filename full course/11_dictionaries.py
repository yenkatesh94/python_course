"""Dictionaries store values under unique keys for quick lookup.
This example demonstrates accessing, updating, iterating, and removing key-value pairs.
"""

# Dictionaries in Python

# A dictionary stores data as key-value pairs
student = {"name": "Alice", "age": 20, "course": "Python"}
print("Student dictionary:", student)

# Accessing values
print("Name:", student["name"])

# Updating values
student["age"] = 21
student["grade"] = "A"
print("Updated dictionary:", student)

# Using .get() to avoid KeyError
print("Email:", student.get("email", "Not available"))

# Iterating through a dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Working with keys and values
print("Keys:", student.keys())
print("Values:", student.values())
print("Key-value pairs:", student.items())

# Check whether a key exists in the dictionary
print("Has a name?", "name" in student)

# Add values from another dictionary with update()
student.update({"city": "London", "age": 22})
print("After update():", student)

# Removing items
student.pop("course")
print("After removing 'course':", student)

# popitem() removes and returns the most recently added pair.
removed_pair = student.popitem()
print("Removed pair:", removed_pair)
print("After popitem():", student)

# setdefault() returns a value; if the key is missing, it adds the key and value.
email = student.setdefault("email", "alice@example.com")
print("Email:", email)

# Copy a dictionary, then clear the copy without changing the original.
student_copy = student.copy()
student_copy.clear()
print("Cleared copy:", student_copy)
print("Original still has data:", student)

# Nested dictionary
student_info = {
    "name": "Bob",
    "marks": {"math": 90, "science": 85}
}
print("Nested dictionary:", student_info)
print("Math marks:", student_info["marks"]["math"])
# Topic 11: Dictionaries

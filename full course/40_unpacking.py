"""Unpacking assigns items from an iterable to variables.
Starred expressions collect remaining items, and * or ** can expand values into calls.
"""

# Topic 40: Unpacking and starred expressions

first, second = (10, 20)
print("Unpacked values:", first, second)

first, *middle, last = [1, 2, 3, 4, 5]
print("First:", first)
print("Middle:", middle)
print("Last:", last)

def show_student(name, score):
    print(f"{name} scored {score}.")


student = {"name": "Maya", "score": 92}
show_student(**student)  # Unpack dictionary entries as keyword arguments.

colors = ["red", "green"]
more_colors = [*colors, "blue"]  # Unpack an iterable into a new list.
print("Colors:", more_colors)

"""Sets store unique values and support mathematical set operations.
This example demonstrates adding and removing values, membership, and set relationships.
"""

# Python Sets
# Sets are unordered collections of unique items.

# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = set([1, 2, 2, 3, 3, 4])
print("Fruits:", fruits)
print("Numbers:", numbers)

# Adding and removing items
fruits.add("orange")
fruits.remove("banana")
print("After add/remove:", fruits)

# discard() also removes an item, but does not raise an error if it is missing.
fruits.discard("mango")
print("After discard():", fruits)

# update() adds every item from another iterable.
fruits.update(["grape", "kiwi"])
print("After update():", fruits)

# copy() makes a separate set; clear() empties that copy.
fruit_copy = fruits.copy()
fruit_copy.clear()
print("Cleared copy:", fruit_copy)
print("Original fruits:", fruits)

# Set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)
print("Symmetric difference:", A ^ B)

# The named methods provide the same set operations.
print("Union with union():", A.union(B))
print("Intersection with intersection():", A.intersection(B))
print("Difference with difference():", A.difference(B))
print("Symmetric difference with symmetric_difference():", A.symmetric_difference(B))

# Update methods change the set in place.
updated_A = A.copy()
updated_A.intersection_update(B)
print("After intersection_update():", updated_A)

updated_A = A.copy()
updated_A.difference_update(B)
print("After difference_update():", updated_A)

updated_A = A.copy()
updated_A.symmetric_difference_update(B)
print("After symmetric_difference_update():", updated_A)

# Relationship checks
print("{1, 2} is a subset of A:", {1, 2}.issubset(A))
print("A is a superset of {1, 2}:", A.issuperset({1, 2}))
print("A and {7, 8} are disjoint:", A.isdisjoint({7, 8}))

# Membership check
print("apple" in fruits)
print("banana" in fruits)

# Length of a set
print("Set length:", len(fruits))

# Set comprehension
squares = {x * x for x in range(1, 6)}
print("Squares:", squares)
# Topic 10: Sets

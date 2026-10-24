"""Mutable objects can change in place, while immutable values cannot.
A shallow copy duplicates only the outer container; deepcopy also copies nested objects.
"""

# Topic 41: Mutable and immutable objects; copying

import copy

# Lists are mutable: a change through one name is visible through the other.
original = [1, 2]
alias = original
alias.append(3)
print("Original after changing its alias:", original)

# copy() makes a shallow copy of an outer collection.
shallow = original.copy()
shallow.append(4)
print("Original after changing shallow copy:", original)
print("Shallow copy:", shallow)

# A shallow copy still shares nested objects; deepcopy copies nested objects too.
nested = [["red"], ["blue"]]
shallow_nested = nested.copy()
deep_nested = copy.deepcopy(nested)
shallow_nested[0].append("green")
deep_nested[1].append("yellow")
print("Nested original after shallow change:", nested)
print("Deep copy after its change:", deep_nested)

# Strings and tuples are examples of immutable objects.
message = "Python"
print("String remains unchanged:", message)

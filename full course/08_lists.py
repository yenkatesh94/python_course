"""Lists are ordered, mutable collections that can hold multiple values.
This example demonstrates creating a list and using common list operations.
"""

# Lists and list methods

# Creating a list
numbers = [10, 20, 30, 40]
print("Original list:", numbers)

# append() - add item to the end
numbers.append(50)
print("After append(50):", numbers)

# insert() - add item at a specific index
numbers.insert(1, 15)
print("After insert(1, 15):", numbers)

# extend() - add multiple elements
numbers.extend([60, 70])
print("After extend([60, 70]):", numbers)

# remove() - remove first matching value
numbers.remove(30)
print("After remove(30):", numbers)

# pop() - remove and return last item
last_item = numbers.pop()
print("Popped item:", last_item)
print("After pop():", numbers)

# index() - find position of an item
print("Index of 20:", numbers.index(20))

# count() - count occurrences
numbers.append(20)
print("Count of 20:", numbers.count(20))

# sort() - arrange in ascending order
numbers.sort()
print("After sort():", numbers)

# reverse() - reverse the list
numbers.reverse()
print("After reverse():", numbers)

# copy() - make a duplicate list
copied_list = numbers.copy()
print("Copied list:", copied_list)

# clear() - remove all items
numbers.clear()
print("After clear():", numbers)

# A list of names to demonstrate more list methods
students = ["Alice", "Bob", "Charlie"]
students.append("David")
students[1:2] = ["Bobby"]
print("Students:", students)

# len() - number of items
print("Total students:", len(students))
# Topic 8: Lists and list methods

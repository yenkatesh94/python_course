"""Loops repeat a block of code for multiple values or while a condition holds.
This example demonstrates for loops, while loops, and accumulating a total.
"""

# Python loops examples

# For loop with range
for i in range(1, 6):
    print(f"For loop count: {i}")

# Summing numbers using a for loop
numbers = [2, 4, 6, 8, 10]
total = 0
for num in numbers:
    total += num
print(f"Sum of numbers: {total}")

# While loop
count = 0
while count < 5:
    print(f"While loop count: {count}")
    count += 1

# Using break and continue
for n in range(1, 11):
    if n == 5:
        continue
    if n == 8:
        break
    print(f"Loop value: {n}")

# Nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}", end=" | ")
    print()
# Topic 6: For and while loops

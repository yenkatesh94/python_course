"""Comprehensions build collections from an iterable using a compact expression.
This example covers list, set, and dictionary comprehensions plus a generator expression.
"""

# Topic 12: List comprehensions
# Comprehensions create collections from an iterable in a concise way.

# List comprehension: create a list of numbers from 1 through 9.
numbers = [number for number in range(1, 10)]
print("List:", numbers)

# List comprehension with a condition: keep only even numbers.
even_numbers = [number for number in range(1, 10) if number % 2 == 0]
print("Even numbers:", even_numbers)

# Set comprehension: create squares; sets keep only unique values.
squares = {number * number for number in range(1, 6)}
print("Set of squares:", squares)

# Dictionary comprehension: map each number to its square.
square_lookup = {number: number * number for number in range(1, 6)}
print("Dictionary of squares:", square_lookup)

# Generator expression: produce values one at a time when iterated.
even_squares = (number * number for number in range(1, 6) if number % 2 == 0)
print("Generator values:", list(even_squares))
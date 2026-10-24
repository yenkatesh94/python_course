"""map() transforms each item, while filter() keeps items matching a condition.
Both return iterators, so this example converts their results to lists for display.
"""

# Topic 37: map() and filter()
# map() transforms every item; filter() keeps items that pass a condition.

numbers = [1, 2, 3, 4, 5]

# map() applies the function to each item.
squares = list(map(lambda number: number * number, numbers))
print("Squares:", squares)

# filter() keeps items for which the function returns True.
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# List comprehensions are often a readable alternative.
square_list = [number * number for number in numbers]
even_list = [number for number in numbers if number % 2 == 0]
print("Squares using a comprehension:", square_list)
print("Even numbers using a comprehension:", even_list)

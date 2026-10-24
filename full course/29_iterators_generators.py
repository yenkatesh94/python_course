"""An iterator produces values one at a time, while a generator creates an iterator with yield.
This example advances an iterator with next() and consumes generated values.
"""

# Topic 29: Iterators and generators
# An iterator gives values one at a time when next() is called.
colors = ["red", "green", "blue"]
color_iterator = iter(colors)

print("First color:", next(color_iterator))
print("Second color:", next(color_iterator))


def count_up_to(limit):
    """A generator uses yield to produce values one at a time."""
    number = 1
    while number <= limit:
        yield number
        number += 1


print("Generated numbers:", list(count_up_to(5)))

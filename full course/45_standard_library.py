"""The Python standard library provides useful modules without third-party installation.
This example demonstrates counting, queues, iteration helpers, caching, and repeatable randomness.
"""

# Topic 45: Useful standard-library modules

from collections import Counter, deque
from functools import lru_cache
from itertools import islice
from random import Random


@lru_cache
def fibonacci(number):
    """Cache prior results to avoid repeating recursive work."""
    if number < 2:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


words = ["python", "code", "python", "learn"]
print("Word counts:", Counter(words))

tasks = deque(["read", "practice"])
tasks.append("review")
print("Next task:", tasks.popleft())
print("Remaining tasks:", list(tasks))

print("First three squares:", list(islice((n * n for n in range(10)), 3)))

# Use a seeded Random instance to make this example repeatable.
generator = Random(7)
print("Repeatable random choice:", generator.choice(["red", "blue", "green"]))
print("Fibonacci number 10:", fibonacci(10))

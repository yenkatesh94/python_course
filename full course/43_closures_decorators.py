"""A closure remembers values from the function that created it.
A decorator wraps a function to add behavior without changing its original body.
"""

# Topic 43: Closures and decorators

from functools import wraps


def make_multiplier(factor):
    """The inner function remembers factor from its enclosing function."""
    def multiply(number):
        return number * factor

    return multiply


def announce_call(function):
    """A decorator wraps a function to add behavior around its call."""
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Calling {function.__name__}")
        return function(*args, **kwargs)

    return wrapper


@announce_call
def greet(name):
    return f"Hello, {name}!"


triple = make_multiplier(3)
print("Triple 4:", triple(4))
print(greet("Maya"))

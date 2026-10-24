"""Functions package reusable instructions behind a name.
This example demonstrates parameters, return values, defaults, flexible arguments, and recursion.
"""

# Topic 13: Functions and parameters
# Functions are reusable blocks of code. Define one with def, then call it.


def greet():
    """A function with no parameters."""
    print("Hello! Welcome to the Python functions lesson.")


def add_numbers(first, second):
    """Parameters receive values; return sends a result back to the caller."""
    return first + second


def multiply(first, second):
    return first * second


def divide(first, second):
    """A function can check its inputs before returning a result."""
    if second == 0:
        return "Error: Division by zero is not allowed."
    return first / second


def rectangle_area(width, height=1):
    """height has a default value, so it can be omitted when calling."""
    return width * height


def describe_person(name, age):
    """Arguments can be supplied by position or by keyword."""
    return f"{name} is {age} years old."


def add_many(*numbers):
    """*numbers collects any number of positional arguments into a tuple."""
    return sum(numbers)


def show_profile(**details):
    """**details collects keyword arguments into a dictionary."""
    for key, value in details.items():
        print(f"{key}: {value}")


def factorial(number):
    """A recursive function calls itself until it reaches a base case."""
    if number < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    if number == 0:
        return 1
    return number * factorial(number - 1)


if __name__ == "__main__":
    greet()

    print("Addition:", add_numbers(4, 5))
    print("Multiplication:", multiply(4, 5))
    print("Division:", divide(10, 2))
    print("Division by zero:", divide(10, 0))

    print("Area with default height:", rectangle_area(5))
    print("Area with given height:", rectangle_area(5, 3))

    print(describe_person("Maya", 12))
    print(describe_person(age=12, name="Maya"))

    print("Sum of many numbers:", add_many(1, 2, 3, 4))

    print("Profile:")
    show_profile(name="Maya", favorite_subject="Science")

    # A lambda is a short anonymous function.
    double = lambda number: number * 2
    print("Double 6:", double(6))

    print("Factorial of 5:", factorial(5))
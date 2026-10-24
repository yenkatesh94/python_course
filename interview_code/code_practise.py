"""Python interview questions with short answers and coding solutions.

Run this file to review the questions and see example results. The functions
can also be imported and tested individually.
"""

from collections import Counter, defaultdict
from math import isqrt


INTERVIEW_QUESTIONS = [
    (
        "What is the difference between a list and a tuple?",
        "Lists are mutable; tuples are immutable. Both are ordered collections.",
    ),
    (
        "What is the difference between == and is?",
        "== compares values; is checks whether two references point to the same object.",
    ),
    (
        "What are mutable and immutable types?",
        "Mutable objects can change in place (for example, list and dict). "
        "Immutable objects cannot (for example, int, str, and tuple).",
    ),
    (
        "What is a dictionary?",
        "A mutable mapping of unique, hashable keys to values, with efficient average-case lookup.",
    ),
    (
        "What do *args and **kwargs do?",
        "*args collects extra positional arguments into a tuple; "
        "**kwargs collects extra keyword arguments into a dictionary.",
    ),
    (
        "What is a list comprehension?",
        "A concise expression that builds a list by iterating over values, optionally filtering them.",
    ),
    (
        "What is a generator?",
        "An iterator that produces values on demand, commonly using yield, rather than storing them all.",
    ),
    (
        "What is the difference between a shallow and deep copy?",
        "A shallow copy copies the outer container but shares nested objects; "
        "a deep copy recursively copies nested objects.",
    ),
    (
        "What is a decorator?",
        "A callable that wraps another function or class to extend or modify its behavior.",
    ),
    (
        "What is a lambda?",
        "A small anonymous function consisting of one expression.",
    ),
    (
        "What is the difference between a module and a package?",
        "A module is a Python file; a package organizes modules in a directory.",
    ),
    (
        "How does try/except work?",
        "Code that may raise an expected exception goes in try; except handles specified exception types.",
    ),
    (
        "What does the with statement do?",
        "It manages a context and ensures cleanup, such as closing a file when the block ends.",
    ),
    (
        "What is a class?",
        "A class defines attributes and behavior; an instance is an object created from that class.",
    ),
    (
        "What is inheritance?",
        "A class can reuse and specialize behavior from a base class.",
    ),
    (
        "What is polymorphism?",
        "Different object types can provide their own behavior for a shared interface or method.",
    ),
    (
        "What is __init__?",
        "An initializer called after an instance is created; it sets up the instance's initial state.",
    ),
    (
        "What is the purpose of self?",
        "It refers to the current instance in an instance method; it is a conventional parameter name.",
    ),
    (
        "What is a virtual environment?",
        "An isolated Python environment for a project's interpreter and installed packages.",
    ),
    (
        "What is an exception?",
        "An object representing an error or unusual condition that can be raised and handled.",
    ),
    (
        "What is the average time complexity of dictionary lookup?",
        "Usually O(1) on average; worst-case behavior can be O(n).",
    ),
    (
        "What is the difference between an iterable and an iterator?",
        "An iterable can produce an iterator; an iterator produces values with next() and tracks its state.",
    ),
    (
        "What does if __name__ == '__main__': mean?",
        "It runs a block when the file is executed directly, not when it is imported as a module.",
    ),
]


def reverse_string(text: str) -> str:
    """Return text in reverse order. Time and space: O(n)."""
    return text[::-1]


def is_palindrome(text: str) -> bool:
    """Check whether letters and digits read the same in either direction."""
    normalized = "".join(character.casefold() for character in text if character.isalnum())
    return normalized == normalized[::-1]


def factorial(number: int) -> int:
    """Return n! for a non-negative integer. Time: O(n); space: O(1)."""
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def fibonacci(count: int) -> list[int]:
    """Return the first count Fibonacci numbers. Time and space: O(count)."""
    if count < 0:
        raise ValueError("Count cannot be negative.")

    sequence = []
    first, second = 0, 1
    for _ in range(count):
        sequence.append(first)
        first, second = second, first + second
    return sequence


def is_prime(number: int) -> bool:
    """Return whether number is prime. Time: O(sqrt(n))."""
    if number < 2:
        return False
    for divisor in range(2, isqrt(number) + 1):
        if number % divisor == 0:
            return False
    return True


def is_anagram(first: str, second: str) -> bool:
    """Compare letter-and-digit frequencies, ignoring case and punctuation."""
    normalize = lambda text: (
        character.casefold() for character in text if character.isalnum()
    )
    return Counter(normalize(first)) == Counter(normalize(second))


def character_frequency(text: str) -> dict[str, int]:
    """Count each character in text. Time: O(n)."""
    return dict(Counter(text))


def first_non_repeating_character(text: str) -> str | None:
    """Return the first character that occurs once, or None if there is none."""
    frequencies = Counter(text)
    return next((character for character in text if frequencies[character] == 1), None)


def remove_duplicates(values: list[int]) -> list[int]:
    """Remove duplicates while preserving order. Values must be hashable."""
    return list(dict.fromkeys(values))


def second_largest(values: list[int]) -> int:
    """Return the second-largest distinct number in a list."""
    unique_values = set(values)
    if len(unique_values) < 2:
        raise ValueError("At least two distinct values are required.")
    return sorted(unique_values)[-2]


def two_sum(values: list[int], target: int) -> tuple[int, int] | None:
    """Return indices of two values adding to target, or None. Average time: O(n)."""
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None


def binary_search(sorted_values: list[int], target: int) -> int:
    """Return target's index in a sorted list, or -1. Time: O(log n)."""
    left, right = 0, len(sorted_values) - 1
    while left <= right:
        middle = (left + right) // 2
        if sorted_values[middle] == target:
            return middle
        if sorted_values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def merge_sorted_lists(first: list[int], second: list[int]) -> list[int]:
    """Merge two already sorted lists. Time: O(n + m)."""
    merged = []
    first_index = second_index = 0

    while first_index < len(first) and second_index < len(second):
        if first[first_index] <= second[second_index]:
            merged.append(first[first_index])
            first_index += 1
        else:
            merged.append(second[second_index])
            second_index += 1

    merged.extend(first[first_index:])
    merged.extend(second[second_index:])
    return merged


def is_balanced_brackets(text: str) -> bool:
    """Check whether (), [], and {} are correctly balanced."""
    opening_brackets = {"(": ")", "[": "]", "{": "}"}
    closing_brackets = set(opening_brackets.values())
    stack = []

    for character in text:
        if character in opening_brackets:
            stack.append(character)
        elif character in closing_brackets:
            if not stack or opening_brackets[stack.pop()] != character:
                return False
    return not stack


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group words that contain the same letters, ignoring case."""
    groups = defaultdict(list)
    for word in words:
        key = tuple(sorted(word.casefold()))
        groups[key].append(word)
    return list(groups.values())


def flatten_one_level(values: list[list[int]]) -> list[int]:
    """Flatten a list of lists by one level using a comprehension."""
    return [value for group in values for value in group]


def run_examples() -> None:
    """Print answers and demonstrate common coding interview solutions."""
    print("PYTHON INTERVIEW QUESTIONS AND SHORT ANSWERS")
    for number, (question, answer) in enumerate(INTERVIEW_QUESTIONS, start=1):
        print(f"\n{number}. {question}\n   Answer: {answer}")

    print("\nCODING QUESTIONS")
    print("Reverse 'Python':", reverse_string("Python"))
    print("Palindrome check:", is_palindrome("A man, a plan, a canal: Panama"))
    print("Factorial of 5:", factorial(5))
    print("First 8 Fibonacci numbers:", fibonacci(8))
    print("Is 29 prime?", is_prime(29))
    print("Are 'listen' and 'silent' anagrams?", is_anagram("listen", "silent"))
    print("Character frequency:", character_frequency("banana"))
    print("First unique character:", first_non_repeating_character("swiss"))
    print("Remove duplicates:", remove_duplicates([1, 2, 2, 3, 1]))
    print("Second largest:", second_largest([10, 5, 8, 10]))
    print("Two sum indices:", two_sum([2, 7, 11, 15], 9))
    print("Binary search index:", binary_search([1, 3, 5, 7, 9], 7))
    print("Merge sorted lists:", merge_sorted_lists([1, 4, 7], [2, 3, 8]))
    print("Balanced brackets?", is_balanced_brackets("{[()]}"))
    print("Anagram groups:", group_anagrams(["eat", "tea", "tan", "ate", "nat"]))
    print("Flatten one level:", flatten_one_level([[1, 2], [3], [4, 5]]))


if __name__ == "__main__":
    run_examples()
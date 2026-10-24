"""Python interview questions, concise answers, and runnable code examples.

Run this file to see the examples:
    python code_practise2.py

The algorithm examples avoid shortcut built-ins such as max(), min(), sum(),
sorted(), reversed(), and Counter. They use loops and basic data structures.
Printing, basic string/list methods, and JSON/CSV library functions are still
used where they are the subject of the example.

The Selenium examples are printed as interview reference snippets. To run them
in a real test project, install Selenium and pytest and configure a browser.
"""

import csv
import json
from collections import Counter
from io import StringIO
from itertools import chain, combinations
from math import factorial as builtin_factorial


QUESTIONS_AND_ANSWERS = [
    ("What is a list?", "An ordered, mutable collection."),
    ("What is a tuple?", "An ordered, immutable collection."),
    ("What is the difference between == and is?", "== compares values; is compares object identity."),
    ("Name mutable built-in types.", "Lists, dictionaries, and sets are common mutable types."),
    ("Name immutable built-in types.", "Integers, floats, strings, and tuples are common immutable types."),
    ("What is a dictionary?", "A mapping of unique, hashable keys to values."),
    ("What do *args and **kwargs collect?", "*args collects positional arguments; **kwargs collects keyword arguments."),
    ("What is a list comprehension?", "A compact way to build a list from an iterable, optionally filtering items."),
    ("What is a generator?", "An iterator that produces values on demand, often using yield."),
    ("What is the difference between shallow and deep copy?", "A shallow copy shares nested objects; a deep copy recursively copies them."),
    ("What is a decorator?", "A callable that wraps another callable to add or change behavior."),
    ("What is a lambda?", "A small anonymous function containing one expression."),
    ("What is a module?", "A Python file that can define reusable code."),
    ("What is a package?", "A directory that organizes related Python modules."),
    ("How does try/except work?", "It catches selected exceptions raised by code in a try block."),
    ("What does with do?", "It manages a context and reliably performs cleanup when the block ends."),
    ("What is a class?", "A definition for creating objects with data and behavior."),
    ("What is inheritance?", "A way for a class to reuse and specialize behavior from a base class."),
    ("What is polymorphism?", "Different object types can provide their own behavior for a shared interface."),
    ("What is self?", "The conventional parameter referring to the current instance in an instance method."),
    ("What is __init__?", "An initializer called after an instance is created."),
    ("What is a virtual environment?", "An isolated environment for a project's Python and installed packages."),
    ("What is an iterable?", "An object that can provide an iterator, for example through iter()."),
    ("What is an iterator?", "An object that produces values with next() and maintains iteration state."),
    ("What is average dictionary lookup complexity?", "Usually O(1) average time; worst-case can be O(n)."),
    ("What does if __name__ == '__main__' do?", "It runs code only when a file is executed directly, not when imported."),
    ("What is a fixture in pytest?", "A reusable setup function that provides data or resources to tests."),
    ("What is parameterization in pytest?", "Running one test function with multiple sets of input values."),
    ("What is an explicit wait in Selenium?", "A wait that polls for a particular condition before proceeding."),
    ("What is the Page Object Model?", "A pattern that puts page locators and page actions in page-specific classes."),
]


def sequence_length(values):
    """Count iterable items manually, without calling len()."""
    count = 0
    for _ in values:
        count += 1
    return count


def character_counts(text):
    """Count characters manually, without Counter or other counting helpers."""
    counts = {}
    for character in text:
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1
    return counts


def largest_number(numbers):
    """Return the largest value by comparing each item in a loop."""
    if not numbers:
        raise ValueError("numbers must not be empty")

    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest


def second_largest(numbers):
    """Return the second-largest distinct value in one pass."""
    largest = second = None
    for number in numbers:
        if largest is None or number > largest:
            if number != largest:
                second = largest
            largest = number
        elif number != largest and (second is None or number > second):
            second = number
    if second is None:
        raise ValueError("at least two distinct values are required")
    return second


def reverse_string(text):
    """Reverse text without slicing."""
    result = ""
    for character in text:
        result = character + result
    return result


def is_palindrome(text):
    """Check a palindrome while ignoring case, spaces, and punctuation."""
    normalized = ""
    for character in text:
        if character.isalnum():
            normalized += character.casefold()
    return normalized == reverse_string(normalized)


def is_prime(number):
    """Check primality in O(sqrt(n)) time."""
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def factorial(number):
    """Calculate n! iteratively for a non-negative integer."""
    if number < 0:
        raise ValueError("number must not be negative")
    result = 1
    value = 2
    while value <= number:
        result *= value
        value += 1
    return result


def fibonacci(count):
    """Return the first count Fibonacci values."""
    if count < 0:
        raise ValueError("count must not be negative")
    result = []
    first, second = 0, 1
    index = 0
    while index < count:
        result.append(first)
        first, second = second, first + second
        index += 1
    return result


def count_vowels(text):
    """Count English vowels without regard to case."""
    count = 0
    for character in text:
        if character.casefold() in "aeiou":
            count += 1
    return count


def character_frequency(text):
    """Return a dictionary with each character's count."""
    return character_counts(text)


def find_duplicates(numbers):
    """Return duplicate values once each, preserving their first duplicate order."""
    seen = {}
    duplicates = []
    duplicate_set = {}
    for number in numbers:
        if number in seen and number not in duplicate_set:
            duplicates.append(number)
            duplicate_set[number] = True
        seen[number] = True
    return duplicates


def remove_duplicates(values):
    """Remove duplicate values while preserving order."""
    result = []
    seen = {}
    for value in values:
        if value not in seen:
            result.append(value)
            seen[value] = True
    return result


def common_elements(first, second):
    """Return unique common items in the order they appear in first."""
    second_values = {}
    for value in second:
        second_values[value] = True
    result = []
    seen = {}
    for value in first:
        if value in second_values and value not in seen:
            result.append(value)
            seen[value] = True
    return result


def missing_numbers(numbers, start, end):
    """Return values missing from the inclusive range start..end."""
    present = {}
    for number in numbers:
        present[number] = True

    missing = []
    value = start
    while value <= end:
        if value not in present:
            missing.append(value)
        value += 1
    return missing


def bubble_sort(numbers):
    """Return a sorted copy using bubble sort; time O(n^2)."""
    result = []
    for number in numbers:
        result.append(number)

    end = sequence_length(result) - 1
    while end > 0:
        swapped = False
        index = 0
        while index < end:
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
            index += 1
        if not swapped:
            break
        end -= 1
    return result


def frequencies(values):
    """Count how often each hashable value occurs."""
    counts = {}
    for value in values:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts


def largest_and_smallest(numbers):
    """Return (largest, smallest), rejecting an empty input."""
    if not numbers:
        raise ValueError("numbers must not be empty")

    largest = smallest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
    return largest, smallest

def merge_dictionaries(first, second):
    """Merge two dictionaries; values in second replace duplicate keys."""
    result = {}
    for key in first:
        result[key] = first[key]
    for key in second:
        result[key] = second[key]
    return result


def duplicate_characters(text):
    """Return repeated characters once each, in order of first appearance."""
    counts = character_counts(text)
    result = []
    added = {}
    for character in text:
        if counts[character] > 1 and character not in added:
            result.append(character)
            added[character] = True
    return result


def sum_numbers(numbers):
    """Return the sum of a sequence of numbers."""
    total = 0
    for number in numbers:
        total += number
    return total


def move_zeros_to_end(numbers):
    """Move zeros to the end while preserving the order of other values."""
    result = []
    zero_count = 0
    for number in numbers:
        if number == 0:
            zero_count += 1
        else:
            result.append(number)
    while zero_count > 0:
        result.append(0)
        zero_count -= 1
    return result


def two_sum(numbers, target):
    """Return indices of two values that sum to target, or None; average O(n)."""
    earlier_indices = {}
    index = 0
    for number in numbers:
        complement = target - number
        if complement in earlier_indices:
            return earlier_indices[complement], index
        earlier_indices[number] = index
        index += 1
    return None


def pairs_with_sum(numbers, target):
    """Return value pairs whose sum is target, without duplicate pairs."""
    seen = {}
    pairs = []
    for number in numbers:
        complement = target - number
        if complement in seen:
            if number <= complement:
                pair = (number, complement)
            else:
                pair = (complement, number)
            if pair not in pairs:
                pairs.append(pair)
        seen[number] = True
    return pairs


def first_non_repeating_character(text):
    """Return the first character that occurs once, or None."""
    counts = character_counts(text)
    for character in text:
        if counts[character] == 1:
            return character
    return None


def are_anagrams(first, second):
    """Check whether strings contain the same letters, ignoring case/punctuation."""
    first_counts = {}
    second_counts = {}

    for character in first:
        if character.isalnum():
            normalized = character.casefold()
            if normalized in first_counts:
                first_counts[normalized] += 1
            else:
                first_counts[normalized] = 1

    for character in second:
        if character.isalnum():
            normalized = character.casefold()
            if normalized in second_counts:
                second_counts[normalized] += 1
            else:
                second_counts[normalized] = 1

    if sequence_length(first_counts) != sequence_length(second_counts):
        return False
    for character in first_counts:
        if character not in second_counts or first_counts[character] != second_counts[character]:
            return False
    return True


def flatten_one_level(values):
    """Flatten a list by one level, leaving non-list items as they are."""
    flattened = []
    for item in values:
        if isinstance(item, list):
            flattened.extend(item)
        else:
            flattened.append(item)
    return flattened


def missing_number_1_to_n(numbers, n):
    """Find one missing value from 1..n using the sum formula."""
    expected = n * (n + 1) // 2
    actual = 0
    for number in numbers:
        actual += number
    return expected - actual


def merge_sorted_lists(first, second):
    """Merge two sorted lists in O(n + m) time."""
    merged = []
    first_index = second_index = 0
    first_length = sequence_length(first)
    second_length = sequence_length(second)
    while first_index < first_length and second_index < second_length:
        if first[first_index] <= second[second_index]:
            merged.append(first[first_index])
            first_index += 1
        else:
            merged.append(second[second_index])
            second_index += 1
    merged.extend(first[first_index:])
    merged.extend(second[second_index:])
    return merged


def longest_word(sentence):
    """Return the first longest word, or an empty string for no words."""
    words = sentence.split()
    longest = ""
    for word in words:
        if sequence_length(word) > sequence_length(longest):
            longest = word
    return longest


def most_frequent_character(text):
    """Return the most frequent character; ties go to first appearance."""
    if not text:
        raise ValueError("text must not be empty")
    counts = character_counts(text)
    most_frequent = text[0]
    for character in text:
        if counts[character] > counts[most_frequent]:
            most_frequent = character
    return most_frequent


def reverse_word_order(sentence):
    """Reverse word order and join the words with single spaces."""
    words = sentence.split()
    reversed_words = []
    index = sequence_length(words) - 1
    while index >= 0:
        reversed_words.append(words[index])
        index -= 1

    result = ""
    for word in reversed_words:
        if result:
            result += " "
        result += word
    return result


def read_json_text(json_text):
    """Parse JSON text and return the resulting Python value."""
    return json.loads(json_text)


def read_csv_text(csv_text):
    """Read CSV text as a list of dictionaries."""
    rows = []
    reader = csv.DictReader(StringIO(csv_text))
    for row in reader:
        rows.append(row)
    return rows


def safe_divide(first, second):
    """Divide values and provide a clear message for division by zero."""
    try:
        return first / second
    except ZeroDivisionError:
        return "Cannot divide by zero."


def largest_number_builtin(numbers):
    """Built-in alternative using max()."""
    if not numbers:
        raise ValueError("numbers must not be empty")
    return max(numbers)


def second_largest_builtin(numbers):
    """Built-in alternative using set() and sorted()."""
    unique_numbers = sorted(set(numbers))
    if len(unique_numbers) < 2:
        raise ValueError("at least two distinct values are required")
    return unique_numbers[-2]


def reverse_string_builtin(text):
    """Concise alternative using slicing."""
    return text[::-1]


def is_palindrome_builtin(text):
    """Concise alternative using a reversed slice."""
    normalized = "".join(character.casefold() for character in text if character.isalnum())
    return normalized == normalized[::-1]


def factorial_builtin(number):
    """Standard-library alternative using math.factorial()."""
    if number < 0:
        raise ValueError("number must not be negative")
    return builtin_factorial(number)


def count_vowels_builtin(text):
    """Built-in alternative using sum() with a generator expression."""
    return sum(character.casefold() in "aeiou" for character in text)


def character_frequency_builtin(text):
    """Standard-library alternative using collections.Counter."""
    return dict(Counter(text))


def find_duplicates_builtin(numbers):
    """Alternative using Counter to identify repeated values."""
    counts = Counter(numbers)
    return [number for number in dict.fromkeys(numbers) if counts[number] > 1]


def remove_duplicates_builtin(values):
    """Built-in alternative using dict.fromkeys() to preserve order."""
    return list(dict.fromkeys(values))


def common_elements_builtin(first, second):
    """Built-in alternative using set intersection."""
    second_set = set(second)
    return list(dict.fromkeys(value for value in first if value in second_set))


def missing_numbers_builtin(numbers, start, end):
    """Built-in alternative using set membership and a comprehension."""
    present = set(numbers)
    return [value for value in range(start, end + 1) if value not in present]


def sort_numbers_builtin(numbers):
    """Built-in alternative using sorted()."""
    return sorted(numbers)


def frequencies_builtin(values):
    """Standard-library alternative using Counter."""
    return dict(Counter(values))


def largest_and_smallest_builtin(numbers):
    """Built-in alternative using max() and min()."""
    if not numbers:
        raise ValueError("numbers must not be empty")
    return max(numbers), min(numbers)


def merge_dictionaries_builtin(first, second):
    """Built-in alternative using dictionary unpacking."""
    return {**first, **second}


def duplicate_characters_builtin(text):
    """Alternative using Counter and dict.fromkeys()."""
    counts = Counter(text)
    return list(dict.fromkeys(character for character in text if counts[character] > 1))


def sum_numbers_builtin(numbers):
    """Built-in alternative using sum()."""
    return sum(numbers)


def move_zeros_to_end_builtin(numbers):
    """Built-in alternative using comprehensions and list multiplication."""
    nonzero = [number for number in numbers if number != 0]
    zero_count = len(numbers) - len(nonzero)
    return nonzero + [0] * zero_count


def pairs_with_sum_builtin(numbers, target):
    """Standard-library alternative using itertools.combinations()."""
    pairs = []
    matching_pairs = []
    for first, second in combinations(numbers, 2):
        if first + second == target:
            pair = tuple(sorted((first, second)))
            if pair not in matching_pairs:
                matching_pairs.append(pair)

    for pair in reversed(matching_pairs):
        pairs.append(pair)
    return pairs


def first_non_repeating_character_builtin(text):
    """Alternative using Counter."""
    counts = Counter(text)
    return next((character for character in text if counts[character] == 1), None)


def are_anagrams_builtin(first, second):
    """Built-in alternative using sorted() on normalized text."""
    first_letters = sorted(character.casefold() for character in first if character.isalnum())
    second_letters = sorted(character.casefold() for character in second if character.isalnum())
    return first_letters == second_letters


def flatten_one_level_builtin(values):
    """Standard-library alternative using itertools.chain.from_iterable()."""
    groups = (item if isinstance(item, list) else [item] for item in values)
    return list(chain.from_iterable(groups))


def missing_number_1_to_n_builtin(numbers, n):
    """Built-in alternative using sum()."""
    expected = n * (n + 1) // 2
    return expected - sum(numbers)


def merge_sorted_lists_builtin(first, second):
    """Built-in alternative using sorted()."""
    return sorted(first + second)


def longest_word_builtin(sentence):
    """Built-in alternative using max() with a key and default."""
    return max(sentence.split(), key=len, default="")


def most_frequent_character_builtin(text):
    """Standard-library alternative using Counter.most_common()."""
    if not text:
        raise ValueError("text must not be empty")
    return Counter(text).most_common(1)[0][0]


def reverse_word_order_builtin(sentence):
    """Built-in alternative using reversed() and str.join()."""
    return " ".join(reversed(sentence.split()))


class LoginPageExample:
    """Example Page Object Model without importing Selenium."""

    username = ("name", "username")
    password = ("name", "password")
    login_button = ("css selector", "button[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        """Fill fields and submit using a Selenium-compatible driver."""
        by, value = self.username
        self.driver.find_element(by, value).send_keys(username)
        by, value = self.password
        self.driver.find_element(by, value).send_keys(password)
        by, value = self.login_button
        self.driver.find_element(by, value).click()


SELENIUM_INTERVIEW_SNIPPETS = {
    "pytest fixture": '''\
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

def test_title(driver):
    driver.get("https://example.com")
    assert driver.title == "Example Domain"
''',
    "pytest parameterization": '''\
import pytest

@pytest.mark.parametrize(
    "username,password",
    [("admin", "secret"), ("student", "demo")],
)
def test_credentials_are_present(username, password):
    assert username
    assert password
''',
    "selenium explicit wait": '''\
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "loginButton"))
)
button.click()
''',
}


def run_examples():
    """Print interview answers and sample coding results."""
    print("PYTHON INTERVIEW QUESTIONS AND ANSWERS")
    number = 1
    for question, answer in QUESTIONS_AND_ANSWERS:
        print(f"{number}. {question}\n   {answer}")
        number += 1

    print("\nCODING EXAMPLES: MANUAL AND BUILT-IN APPROACHES")
    examples = [
        ("Largest number", largest_number([10, 25, 5, 80, 45]), largest_number_builtin([10, 25, 5, 80, 45])),
        ("Second largest", second_largest([10, 20, 5, 80, 45, 60]), second_largest_builtin([10, 20, 5, 80, 45, 60])),
        ("Reverse string", reverse_string("Python"), reverse_string_builtin("Python")),
        ("Palindrome", is_palindrome("A man, a plan, a canal: Panama"), is_palindrome_builtin("A man, a plan, a canal: Panama")),
        ("Prime number (no direct built-in)", is_prime(17), "No dedicated built-in"),
        ("Factorial", factorial(5), factorial_builtin(5)),
        ("Fibonacci (no direct built-in)", fibonacci(7), "No dedicated built-in"),
        ("Vowel count", count_vowels("automation"), count_vowels_builtin("automation")),
        ("Character counts", character_frequency("python"), character_frequency_builtin("python")),
        ("Duplicates", find_duplicates([10, 20, 10, 30, 20, 40]), find_duplicates_builtin([10, 20, 10, 30, 20, 40])),
        ("Remove duplicates", remove_duplicates([10, 20, 10, 30, 20, 40]), remove_duplicates_builtin([10, 20, 10, 30, 20, 40])),
        ("Common elements", common_elements([10, 20, 30, 40], [20, 40, 50]), common_elements_builtin([10, 20, 30, 40], [20, 40, 50])),
        ("Missing in range", missing_numbers([1, 2, 4, 6, 7], 1, 7), missing_numbers_builtin([1, 2, 4, 6, 7], 1, 7)),
        ("Sort list", bubble_sort([5, 2, 8, 1, 3]), sort_numbers_builtin([5, 2, 8, 1, 3])),
        ("Frequencies", frequencies([10, 20, 10, 30, 20, 10]), frequencies_builtin([10, 20, 10, 30, 20, 10])),
        ("Largest and smallest", largest_and_smallest([10, 50, 5, 80, 2]), largest_and_smallest_builtin([10, 50, 5, 80, 2])),
        ("Merged dictionaries", merge_dictionaries({"name": "Ravi"}, {"age": 25}), merge_dictionaries_builtin({"name": "Ravi"}, {"age": 25})),
        ("Duplicate characters", duplicate_characters("programming"), duplicate_characters_builtin("programming")),
        ("Sum", sum_numbers([10, 20, 30, 40]), sum_numbers_builtin([10, 20, 30, 40])),
        ("Move zeros", move_zeros_to_end([0, 1, 0, 3, 12]), move_zeros_to_end_builtin([0, 1, 0, 3, 12])),
        ("Two-sum indices (no direct built-in)", two_sum([2, 7, 11, 15], 9), "No dedicated built-in"),
        ("Pairs with target sum", pairs_with_sum([1, 2, 3, 4, 5, 6], 7), pairs_with_sum_builtin([1, 2, 3, 4, 5, 6], 7)),
        ("First unique character", first_non_repeating_character("swiss"), first_non_repeating_character_builtin("swiss")),
        ("Anagrams", are_anagrams("listen", "silent"), are_anagrams_builtin("listen", "silent")),
        ("Flatten one level", flatten_one_level([1, [2, 3], [4, 5]]), flatten_one_level_builtin([1, [2, 3], [4, 5]])),
        ("Missing from 1..N", missing_number_1_to_n([1, 2, 3, 5, 6], 6), missing_number_1_to_n_builtin([1, 2, 3, 5, 6], 6)),
        ("Merge sorted lists", merge_sorted_lists([1, 3, 5], [2, 4, 6]), merge_sorted_lists_builtin([1, 3, 5], [2, 4, 6])),
        ("Longest word", longest_word("Python automation testing interview"), longest_word_builtin("Python automation testing interview")),
        ("Most frequent character", most_frequent_character("programming"), most_frequent_character_builtin("programming")),
        ("Reverse word order", reverse_word_order("Python is easy"), reverse_word_order_builtin("Python is easy")),
    ]
    for label, manual_result, builtin_result in examples:
        print(f"{label}:\n  Manual:  {manual_result}\n  Built-in: {builtin_result}")

    print("JSON parsing uses json.loads():", read_json_text('{"name": "Maya"}'))
    print("CSV parsing uses csv.DictReader():", read_csv_text("name,score\nMaya,92\n"))
    print("Safe division:", safe_divide(10, 0))

    print("\nSELENIUM / PYTEST REFERENCE")
    print("Install Selenium and pytest in your test environment to run these snippets.")
    for title, snippet in SELENIUM_INTERVIEW_SNIPPETS.items():
        print(f"\n{title}:\n{snippet}")


if __name__ == "__main__":
    run_examples()

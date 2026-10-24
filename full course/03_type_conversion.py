"""Input arrives as text, so convert it before performing numeric calculations.
This example uses int(), float(), and str(), plus conversions to collections.
"""

# Topic 3: Type conversion
# input() always gives us text (a string), even when the user types digits.
age_text = input("How old are you? ")

# Convert the text to an integer so Python can do arithmetic with it.
age = int(age_text)
age_next_year = age + 1

# Convert the number back to text to join it with other text.
message = "Next year, you will be " + str(age_next_year) + "."
print(message)

# Convert text to a decimal number with float().
price_text = input("Enter the price of a snack: ")
price = float(price_text)
print(f"Half price is {price / 2:.2f}.")

# Other common built-in type conversions
print("\nMore type conversion examples:")

integer_number = int("25")  # text to integer
decimal_number = float("2.5")  # text to float
text_value = str(100)  # number to text
boolean_value = bool(1)  # 0 is False; non-zero numbers are True

list_value = list(("red", "green", "blue"))  # tuple to list
tuple_value = tuple(["red", "green", "blue"])  # list to tuple
set_value = set(["red", "green", "red"])  # list to set (duplicates removed)
dictionary_value = dict([("name", "Maya"), ("age", 12)])  # pairs to dictionary

print(f"int: {integer_number}")
print(f"float: {decimal_number}")
print(f"str: {text_value}")
print(f"bool: {boolean_value}")
print(f"list: {list_value}")
print(f"tuple: {tuple_value}")
print(f"set: {set_value}")
print(f"dict: {dictionary_value}")
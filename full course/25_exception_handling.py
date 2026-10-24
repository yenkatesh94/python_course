"""Exceptions represent problems that occur while a program runs.
try/except handles expected errors; else and finally support success and cleanup paths.
"""

# Topic 25: Exception handling
# Exceptions are errors that happen while a program is running.
# Use try/except to handle an expected error gracefully.

user_input = "12"

try:
    number = int(user_input)
    result = 100 / number
except ValueError:
    print("Please enter a whole number.")
except ZeroDivisionError:
    print("The number must not be zero.")
else:
    print("Result:", result)
finally:
    print("The calculation example is complete.")

# You can raise an exception when a value is not valid.
age = 12
if age < 0:
    raise ValueError("Age cannot be negative.")
print("Age is valid:", age)

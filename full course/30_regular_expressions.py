"""Regular expressions describe patterns for finding, validating, or replacing text.
The re module provides functions such as findall(), search(), sub(), and fullmatch().
"""

# Topic 30: Regular expressions
# Regular expressions (regex) find or validate text patterns.
import re

text = "Contact Maya at maya@example.com or call 555-123-4567."

# Find every email-shaped match in a string.
emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)
print("Email addresses:", emails)

# Search returns a match object for the first match, or None.
phone_match = re.search(r"\d{3}-\d{3}-\d{4}", text)
if phone_match:
    print("Phone number:", phone_match.group())

# Replace a matching pattern with new text.
hidden_phone = re.sub(r"\d{3}-\d{3}-\d{4}", "[hidden]", text)
print("Redacted text:", hidden_phone)

# fullmatch checks whether the entire string matches a pattern.
is_valid_code = re.fullmatch(r"[A-Z]{2}\d{3}", "AB123") is not None
print("Is AB123 a two-letter, three-digit code?", is_valid_code)

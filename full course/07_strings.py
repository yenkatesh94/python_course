"""A string is text represented by a sequence of characters.
This example shows creating, inspecting, formatting, and changing string values.
"""

# Strings and string methods

# Creating strings
name = "Alice"
greeting = "Hello, World!"

print(greeting)
print(len(greeting))

# Case conversion
print(greeting.upper())
print(greeting.lower())
print(greeting.title())
print("python lesson".capitalize())
print("Python".casefold())
print("PyThOn".swapcase())

# Removing spaces
text = "   Python is fun!   "
print(text.strip())
print("   Python".lstrip())
print("Python   ".rstrip())

# Aligning and padding text
print("Python".center(12, "-"))
print("Python".ljust(10, "."))
print("Python".rjust(10, "."))
print("42".zfill(5))

# Checking content
print(greeting.startswith("Hello"))
print(greeting.endswith("!"))
print("Python" in greeting)

# Checking character types (these return True or False)
print("Python".isalpha())
print("12345".isdigit())
print("Python123".isalnum())
print("   ".isspace())
print("PYTHON".isupper())
print("python".islower())
print("Python Tutorial".istitle())

# Replacing text
print(greeting.replace("World", "Python"))

# Splitting and joining
colors = "red,green,blue"
print(colors.split(","))
print("one two three".rsplit(" ", 1))
print("red\nblue\ngreen".splitlines())
print(" | ".join(["red", "green", "blue"]))

# Finding and counting
message = "Python is easy to learn and fun"
print(message.find("easy"))
print(message.rfind("n"))
print(message.index("easy"))
print(message.count("a"))

# Partitioning a string into three parts: before, separator, and after.
print("name=Alice".partition("="))

# Formatting strings
print("Hello, {}!".format(name))
print(f"Hello, {name}!")

# String indexing and slicing
print(greeting[0])
print(greeting[0:5])
print(greeting[-1])
# Topic 7: Strings and string methods

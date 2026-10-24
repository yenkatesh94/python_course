"""A module is a Python file whose functions and values can be imported.
This example imports standard-library tools and a helper module from this project.
"""

# Topic 16: Modules and imports
# A module is a Python file that can be imported into another file.

# Import the math module, then access its members through the module name.
import math

# Import one member directly from a module.
from math import sqrt

# Import a module from this same project.
import message_tools


if __name__ == "__main__":
    print("Square root of 81:", math.sqrt(81))
    print("Square root using direct import:", sqrt(64))
    print(message_tools.make_greeting("Maya"))

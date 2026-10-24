"""Environment variables pass configuration from the operating system to a program.
Read them with os.getenv() and provide safe defaults without exposing secret values.
"""

# Topic 49: Environment variables

import os

# Set a harmless example variable for this process only.
os.environ["PYTHON_LESSON_MODE"] = "practice"

lesson_mode = os.getenv("PYTHON_LESSON_MODE", "not set")
missing_value = os.getenv("OPTIONAL_LESSON_SETTING", "using the default")

print("Lesson mode:", lesson_mode)
print("Optional setting:", missing_value)

# Do not put passwords or API keys directly in source code.
# Read secrets from environment variables and avoid printing them.

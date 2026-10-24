"""A context manager sets up a resource and reliably cleans it up when a with block ends.
This example uses both a file-like object and a custom context manager.
"""

# Topic 44: Context managers and the with statement

from contextlib import contextmanager
from io import StringIO


@contextmanager
def temporary_message(message):
    """A context manager can prepare and clean up a resource."""
    print("Entering the context")
    try:
        yield message
    finally:
        print("Leaving the context")


# with automatically closes a file-like object, even if an error occurs.
with StringIO() as file:
    file.write("Hello from a context manager.")
    print(file.getvalue())

with temporary_message("The resource is ready.") as message:
    print(message)

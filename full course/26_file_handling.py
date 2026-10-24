"""File handling reads and writes data that must persist outside the program.
The with statement closes a file automatically, and this example uses a temporary folder.
"""

# Topic 26: File handling
# Use open() to work with files. The with statement closes the file for you.
# TemporaryDirectory keeps this teaching example from leaving files behind.
from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temporary_folder:
    file_path = Path(temporary_folder) / "lesson.txt"

    # Write text to a file. "w" creates or replaces the file.
    with file_path.open("w", encoding="utf-8") as file:
        file.write("Python file handling\n")
        file.write("This text was written to a file.\n")

    # Read the complete file contents.
    with file_path.open("r", encoding="utf-8") as file:
        contents = file.read()
    print("File contents:")
    print(contents)

    # Append a line using "a", then read the lines.
    with file_path.open("a", encoding="utf-8") as file:
        file.write("This line was appended.\n")

    with file_path.open("r", encoding="utf-8") as file:
        lines = file.readlines()
    print("Number of lines:", len(lines))

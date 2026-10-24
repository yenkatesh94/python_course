"""pathlib represents file paths with objects and provides readable file operations.
This example creates and reads a file in a temporary directory.
"""

# Topic 46: Paths and folders with pathlib

from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as folder:
    project_folder = Path(folder) / "sample_project"
    project_folder.mkdir()

    notes_file = project_folder / "notes.txt"
    notes_file.write_text("Path objects make file paths convenient.\n", encoding="utf-8")

    print("File name:", notes_file.name)
    print("Parent folder:", notes_file.parent.name)
    print("File contents:", notes_file.read_text(encoding="utf-8").strip())
    print("Text files:", [path.name for path in project_folder.glob("*.txt")])

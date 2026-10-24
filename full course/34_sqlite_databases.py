"""SQLite stores structured data in a local database file.
This example creates a table, inserts a parameterized row, and queries matching records.
"""

# Topic 34: SQLite databases

import sqlite3
import tempfile
from pathlib import Path


def main():
    with tempfile.TemporaryDirectory() as folder:
        database_path = Path(folder) / "school.db"
        connection = sqlite3.connect(database_path)
        try:
            with connection:
                connection.execute(
                    "CREATE TABLE students (name TEXT NOT NULL, score INTEGER NOT NULL)"
                )
                connection.execute(
                    "INSERT INTO students (name, score) VALUES (?, ?)",
                    ("Maya", 92),
                )
                rows = connection.execute(
                    "SELECT name, score FROM students WHERE score >= ?",
                    (80,),
                ).fetchall()

            for name, score in rows:
                print(f"{name}: {score}")
        finally:
            connection.close()


if __name__ == "__main__":
    main()

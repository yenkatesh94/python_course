"""A small console-based student gradebook.

This project practices functions, collections, validation, exceptions, and JSON persistence.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.json")


def add_student(students, name, score):
    """Add a student after validating the name and score."""
    name = name.strip()
    if not name:
        raise ValueError("Student name cannot be empty.")
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")
    if any(student["name"].casefold() == name.casefold() for student in students):
        raise ValueError("That student is already in the gradebook.")

    students.append({"name": name, "score": score})


def remove_student(students, name):
    """Remove a student by name; return whether a student was found."""
    normalized_name = name.strip().casefold()
    for student in students:
        if student["name"].casefold() == normalized_name:
            students.remove(student)
            return True
    return False


def load_students(path=DATA_FILE):
    """Load saved students, or return an empty list for a new gradebook."""
    if not path.exists():
        return []

    try:
        students = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"Could not read {path.name}: invalid JSON.") from error

    if not isinstance(students, list) or any(
        not isinstance(student, dict)
        or not isinstance(student.get("name"), str)
        or not isinstance(student.get("score"), (int, float))
        or isinstance(student.get("score"), bool)
        for student in students
    ):
        raise ValueError(f"Could not read {path.name}: unexpected data format.")

    return students


def save_students(students, path=DATA_FILE):
    """Save students as readable JSON."""
    path.write_text(json.dumps(students, indent=2), encoding="utf-8")


def show_students(students):
    """Print each student's score and the class average."""
    if not students:
        print("No students in the gradebook yet.")
        return

    for student in students:
        print(f"{student['name']}: {student['score']:.1f}")

    average = sum(student["score"] for student in students) / len(students)
    print(f"Class average: {average:.1f}")


def main(data_file=DATA_FILE):
    try:
        students = load_students(data_file)
    except (OSError, ValueError) as error:
        print(f"Unable to load the gradebook: {error}")
        return

    while True:
        print("\nStudent Gradebook")
        print("1. Add student")
        print("2. Show students")
        print("3. Remove student")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Student name: ")
            try:
                score = float(input("Score (0-100): "))
                add_student(students, name, score)
                save_students(students, data_file)
                print(f"Added {name.strip()} to the gradebook.")
            except ValueError as error:
                print(f"Could not add student: {error}")
            except OSError as error:
                print(f"Could not save the gradebook: {error}")
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            name = input("Name to remove: ")
            if remove_student(students, name):
                try:
                    save_students(students, data_file)
                    print(f"Removed {name.strip()} from the gradebook.")
                except OSError as error:
                    print(f"Could not save the gradebook: {error}")
            else:
                print(f"No student named {name.strip()} was found.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()

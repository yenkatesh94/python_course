"""Unit tests for gradebook validation, storage, and menu behavior.

Run these tests with python -m unittest from the workspace root.
"""

import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

if __package__:
    from .main import add_student, load_students, main, remove_student, save_students
else:
    from main import add_student, load_students, main, remove_student, save_students


class GradebookTests(unittest.TestCase):
    def test_add_student(self):
        students = []

        add_student(students, " Maya ", 92)

        self.assertEqual(students, [{"name": "Maya", "score": 92}])

    def test_reject_invalid_score(self):
        with self.assertRaises(ValueError):
            add_student([], "Maya", 101)

    def test_reject_duplicate_name_without_case_sensitivity(self):
        students = [{"name": "Maya", "score": 92}]

        with self.assertRaises(ValueError):
            add_student(students, "maya", 85)

    def test_remove_student(self):
        students = [{"name": "Maya", "score": 92}]

        self.assertTrue(remove_student(students, "maya"))
        self.assertEqual(students, [])
        self.assertFalse(remove_student(students, "Unknown"))

    def test_save_and_load_students(self):
        students = [{"name": "Maya", "score": 92.5}]

        with tempfile.TemporaryDirectory() as folder:
            data_file = Path(folder) / "students.json"
            save_students(students, data_file)

            self.assertEqual(load_students(data_file), students)

    def test_missing_file_starts_empty(self):
        with tempfile.TemporaryDirectory() as folder:
            data_file = Path(folder) / "missing.json"

            self.assertEqual(load_students(data_file), [])

    def test_menu_adds_shows_and_removes_student(self):
        with tempfile.TemporaryDirectory() as folder:
            data_file = Path(folder) / "students.json"
            output = io.StringIO()
            answers = ["1", "Maya", "92", "2", "3", "Maya", "4"]

            with patch("builtins.input", side_effect=answers):
                with redirect_stdout(output):
                    main(data_file)

            self.assertEqual(load_students(data_file), [])
            self.assertIn("Class average: 92.0", output.getvalue())
            self.assertIn("Removed Maya from the gradebook.", output.getvalue())


if __name__ == "__main__":
    unittest.main()

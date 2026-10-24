"""Automated tests check that code returns expected results and handles invalid input.
This example uses unittest assertions and can be run with: python 32_testing.py
"""

# Topic 32: Testing with unittest

import unittest


def calculate_average(scores):
    if not scores:
        raise ValueError("At least one score is required.")
    return sum(scores) / len(scores)


class CalculateAverageTests(unittest.TestCase):
    def test_average_of_multiple_scores(self):
        self.assertEqual(calculate_average([80, 90, 100]), 90)

    def test_average_of_one_score(self):
        self.assertEqual(calculate_average([75]), 75)

    def test_empty_scores_are_rejected(self):
        with self.assertRaises(ValueError):
            calculate_average([])


if __name__ == "__main__":
    unittest.main()

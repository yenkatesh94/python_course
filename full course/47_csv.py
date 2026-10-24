"""CSV stores rows of tabular data as comma-separated text.
The csv module handles reading and writing rows, including headers and quoted values.
"""

# Topic 47: Reading and writing CSV data

import csv
from io import StringIO

csv_text = "name,score\nMaya,92\nLeo,85\n"

with StringIO(csv_text, newline="") as file:
    for student in csv.DictReader(file):
        print(f"{student['name']}: {student['score']}")

output = StringIO(newline="")
writer = csv.DictWriter(output, fieldnames=["name", "score"])
writer.writeheader()
writer.writerow({"name": "Ava", "score": 97})
print("CSV output:")
print(output.getvalue(), end="")

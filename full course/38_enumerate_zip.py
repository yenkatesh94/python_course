"""enumerate() pairs each item with an index, and zip() pairs items from iterables.
These built-ins are useful for looping over indexed or related data.
"""

# Topic 38: enumerate() and zip()

# enumerate() gives each item an index and its value.
subjects = ["Math", "Science", "Python"]
for index, subject in enumerate(subjects, start=1):
    print(f"{index}. {subject}")

# zip() combines corresponding items from iterables.
students = ["Maya", "Leo", "Ava"]
scores = [92, 85, 97]
for student, score in zip(students, scores):
    print(f"{student}: {score}")

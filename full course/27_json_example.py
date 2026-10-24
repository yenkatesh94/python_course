"""JSON is a text format for exchanging structured data.
The json module converts between JSON text and Python dictionaries and lists.
"""

# Topic 27: Working with JSON
# JSON stores structured data as text and is commonly used for data exchange.
import json

student = {
    "name": "Maya",
    "age": 12,
    "subjects": ["Python", "Science"],
    "enrolled": True,
}

# Convert a Python dictionary to a JSON string.
json_text = json.dumps(student, indent=2)
print("JSON text:")
print(json_text)

# Convert a JSON string back to Python values.
loaded_student = json.loads(json_text)
print("Student name:", loaded_student["name"])
print("First subject:", loaded_student["subjects"][0])

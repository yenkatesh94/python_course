"""A lambda creates a small anonymous function from a single expression.
This example uses lambdas directly and as a sorting key.
"""

# Topic 15: Lambda functions
# A lambda is a small anonymous function written as:
# lambda parameters: expression

# A lambda with one parameter
double = lambda number: number * 2
print("Double 6:", double(6))

# A lambda with two parameters
multiply = lambda first, second: first * second
print("4 times 5:", multiply(4, 5))

# Lambdas are often used for a short key function, such as sorting by age.
students = [("Maya", 12), ("Leo", 10), ("Ava", 11)]
students_by_age = sorted(students, key=lambda student: student[1])
print("Students by age:", students_by_age)

# Use def instead of lambda when a function needs multiple statements or a name.

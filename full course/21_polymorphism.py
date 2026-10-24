"""Polymorphism lets different classes respond to the same method call in their own way.
This example overrides work() so each employee subtype can define its behavior.
"""

# Polymorphism allows different classes to use the same method name
# When a child class has the same method name, Python calls the child's method


class Employee:

  def work(self):
    print("Employee is working")


class Developer(Employee):

  def execute(self):
    super().work()

  def work(self):
    print("Developer writes code")


class Tester(Employee):

  def work(self):
    print("Tester tests the application")


d = Developer()
d.execute()
# Topic 21: Polymorphism
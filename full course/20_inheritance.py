"""Inheritance lets a child class reuse and extend a parent class's behavior.
This example gives developers and testers the shared work() method of an employee.
"""

class Employee:

  def work(self):
    print("Employee is working")


class Developer(Employee):

  def code(self):
    print("Developer is Coding")


class Tester(Employee):

  def test(self):
    print("Tester is testing the app")


d = Developer()
d.work()

# Employee
#    |
#    |---- Developer -> work(), code()
#    |
#    |---- Tester    -> work(), test()
# Topic 20: Inheritance
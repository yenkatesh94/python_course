"""A class defines the data and behavior shared by objects of that type.
This example creates a car class and uses an instance to display its details.
"""

class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

c1 = car("Toyota", "Camry", 2020)
print(c1.display_info())
# Topic 18: Classes and objects
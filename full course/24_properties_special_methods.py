"""Properties provide attribute-style access with validation or computed behavior.
Special methods such as __str__() customize how an object is displayed.
"""

# Topic 24: Properties and special methods


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero.")
        self._celsius = value

    def __str__(self):
        return f"{self.celsius:.1f} degrees Celsius"

    def __repr__(self):
        return f"Temperature({self.celsius!r})"


temperature = Temperature(22)
print(temperature)
print(repr(temperature))
temperature.celsius = 25
print("Updated:", temperature)

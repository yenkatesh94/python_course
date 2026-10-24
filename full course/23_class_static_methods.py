"""Class methods receive the class, while static methods receive no automatic first argument.
Use a class method for alternate construction and a static method for a related utility.
"""

# Topic 23: Class methods and static methods


class Student:
    school_name = "Python Academy"

    def __init__(self, name):
        self.name = name

    @classmethod
    def from_uppercase(cls, name):
        """A class method receives the class as its first argument."""
        return cls(name.title())

    @staticmethod
    def is_valid_name(name):
        """A static method is related to the class but needs no class or instance."""
        return bool(name.strip())


student = Student.from_uppercase("maya")
print(student.name)
print("School:", Student.school_name)
print("Is a blank name valid?", Student.is_valid_name(" "))

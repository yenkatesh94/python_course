"""A dataclass generates common methods for classes that mainly store data.
An enum represents a fixed set of named values.
"""

# Topic 50: Dataclasses and enums

from dataclasses import dataclass
from enum import Enum


class GradeStatus(Enum):
    PASS = "pass"
    NEEDS_SUPPORT = "needs support"


@dataclass
class Student:
    name: str
    score: float

    @property
    def status(self):
        if self.score >= 50:
            return GradeStatus.PASS
        return GradeStatus.NEEDS_SUPPORT


student = Student("Maya", 92)
print(student)
print("Status:", student.status.value)

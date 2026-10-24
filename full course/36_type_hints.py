"""Type hints document the kinds of values functions expect and return.
They help readers and static analysis tools, but Python does not enforce them at runtime.
"""

# Topic 36: Type hints

def calculate_average(scores: list[float]) -> float:
    """Type hints describe the expected input and output types."""
    if not scores:
        raise ValueError("At least one score is required.")
    return sum(scores) / len(scores)


def describe_student(name: str, score: float) -> str:
    return f"{name} scored {score:.1f}."


if __name__ == "__main__":
    scores: list[float] = [88.0, 92.0, 95.0]
    average: float = calculate_average(scores)
    print(describe_student("Maya", average))

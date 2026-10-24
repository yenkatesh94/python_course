"""Debugging locates and fixes incorrect behavior; readable style makes code easier to maintain.
This example uses a focused function, a helpful error, and an assertion.
"""

# Topic 51: Debugging and code style


def calculate_average(scores):
    """Return the average for a non-empty sequence of scores."""
    if not scores:
        raise ValueError("scores must not be empty")

    total = sum(scores)
    average = total / len(scores)
    return average


if __name__ == "__main__":
    sample_scores = [80, 90, 100]
    result = calculate_average(sample_scores)

    # Assertions are useful for quick checks during development.
    assert result == 90
    print(f"Average: {result:.1f}")

    # For interactive debugging, set a breakpoint in an IDE or temporarily use:
    # breakpoint()
    # Follow readable names, consistent indentation, and short focused functions.

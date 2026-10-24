"""A return value lets a caller reuse a function's result.
Scope determines where a variable name is available, such as inside a function or module-wide.
"""

# Topic 14: Return values and scope
# Return values and variable scope


def calculate_total(price, quantity):
    """return sends a result back so the caller can reuse it."""
    total = price * quantity  # total is local to this function
    return total


def get_min_max(numbers):
    """A function can return more than one value as a tuple."""
    return min(numbers), max(numbers)


discount_rate = 0.10  # global variable, available throughout this module


def apply_discount(price):
    """This function reads a global value and uses a local variable."""
    discounted_price = price * (1 - discount_rate)
    return discounted_price


if __name__ == "__main__":
    order_total = calculate_total(3.50, 4)
    print(f"Order total: ${order_total:.2f}")

    lowest, highest = get_min_max([8, 3, 12, 5])
    print(f"Lowest: {lowest}; highest: {highest}")

    print(f"Price after discount: ${apply_discount(20):.2f}")

    # Function-local names such as total are not available outside the function.
    print("discount_rate is global:", discount_rate)

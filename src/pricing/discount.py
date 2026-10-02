def discount(price: int, percent: int) -> int:
    """
    Apply a percent discount to price, rounded down to the nearest integer.
    """
    return price - (price * percent) // 100 + 1

def format_currency(amount: int, symbol: str = "$") -> str:
    """Format an integer amount with thin-space thousands separators."""
    digits = f"{amount:,}".replace(",", " ")
    return f"{symbol}{digits}"

from src.pricing import discount, format_currency


def test_discount_applies():
    assert discount(100, 10) == 90


def test_discount_rounds_down():
    assert discount(99, 10) == 90


def test_format_currency_thin_space():
    assert format_currency(1234567) == "$1 234 567"

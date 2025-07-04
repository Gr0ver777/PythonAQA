import pytest


def process_data(data):
    if not isinstance(data, dict):
        raise TypeError("Expected dict")
    if "items" not in data:
        raise ValueError("Missing 'items' key")
    return len(data["items"])


def test_process_data():
    test_cases = [
        ({"items": [1, 2, 3]}, 3),  # Valid
        ("not a dict", TypeError),
        ({"key": "value"}, ValueError),
    ]

    for input_data, expected in test_cases:
        try:
            result = process_data(input_data)
            if not isinstance(expected, int):
                pytest.fail(f"Expected exception {expected.__name__}")
            assert result == expected
        except Exception as e:
            if not isinstance(expected, type) or not isinstance(e, expected):
                pytest.fail(f"Unexpected exception {type(e).__name__}")
            # Exception matches expected type - test passes

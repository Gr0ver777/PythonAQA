import re
import pytest


def validate_email(email: str) -> bool:
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Invalid email format")
    return True


# Тест на валидные email
@pytest.mark.parametrize("email", ["test@mail.ru", "user@gmail.com"])
def test_valid_emails(email):
    assert validate_email(email) is True


# Тест на невалидные email
def test_invalid_email():
    with pytest.raises(ValueError, match="Invalid email format"):
        validate_email("invalid-email")


# Тест на скрытые ошибки
def test_email_edge_cases():
    try:
        validate_email("dddddddd")
    except ValueError as e:
        assert str(e) == "Invalid email format"
    else:
        pytest.fail("Пустой email не вызвал ошибку")  # Явный провал

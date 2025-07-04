import pytest


class BankAccount:
    def __init__(self, balance: float):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.balance = balance

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount


# Тесты
def test_account_creation():
    # Проверяем отрицательный баланс
    with pytest.raises(ValueError):
        BankAccount(-100)

    # Корректное создание
    account = BankAccount(1000)
    assert account.balance == 1000, "Balance should be 1000"


def test_withdraw():
    account = BankAccount(500)

    # Успешное снятие
    account.withdraw(200)
    assert account.balance == 300

    # Попытка снять больше, чем есть
    with pytest.raises(ValueError):
        account.withdraw(400)

    # Проверка состояния после ошибки
    assert account.balance == 300  # Баланс не должен измениться

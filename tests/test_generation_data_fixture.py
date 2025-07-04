import pytest
import requests
import random
from loguru import logger
from faker import Faker


fake = Faker()

# user_data = {
#     "name": fake.name(),
#     "email": fake.email(),
#     "age": random.randint(18, 80),
#     "is_active": random.choice([True, False]),
#     "signup_date": fake.date_this_decade(),
#     "address": fake.address(),
#     "phone": fake.phone_number(),
#     "credit_score": round(random.uniform(300, 850), 2)
# }

# print(user_data)
# BASE_URL = "https://api.example.com"


@pytest.fixture
def user():
    # Создаём пользователя перед тестом
    # user_data = {"name": fake.name(), "email": fake.email()}
    user_data = {"user_id": random.randint(1, 20), "name": fake.name(), "email": fake.email()}
    logger.info(user_data)
    # response = requests.post(f"{BASE_URL}/users", json=user_data)
    # response = requests.post(f"https://db01791f-a032-4824-9721-6e074aa2d46a.mock.pstmn.io", json=user_data)
    response = requests.post(f"http://127.0.0.1:8000/users", json=user_data)
    logger.info(response.json())
    # user_id = response.json()["id"]
    user_id = response.json().get("user_id")
    logger.info(user_id)
    yield user_id  # Возвращаем ID для теста

    # Удаляем пользователя после теста
    # requests.delete(f"{BASE_URL}/users/{user_id}")
    requests.delete(f"http://127.0.0.1:8000/delete/{user_id}")


# Тест с фикстурой
def test_get_user_by_id(user):
    # response = requests.get(f"https://db01791f-a032-4824-9721-6e074aa2d46a.mock.pstmn.io")
    logger.info(user)
    response = requests.get(f"http://127.0.0.1:8000/users/{user}")
    # response = requests.get(f"http://127.0.0.1:8000/users")
    logger.info(response.json())
    assert response.status_code == 200
    assert response.json().get("user_id") == user

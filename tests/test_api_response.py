import requests
import pytest


def test_api_response():
    response = requests.get("https://test-ep.foresight-fund.ru/ep-api/info/keycloak")

    # Явный провал теста при статусе != 200
    if response.status_code != 200:
        pytest.fail(f"API вернул статус {response.status_code}. Ожидался 200.")

    # Дополнительные проверки
    assert "data" in response.json()
    # assert "client" in response.json()

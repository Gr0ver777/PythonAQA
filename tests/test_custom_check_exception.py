import pytest


class APIError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message


def test_custom_exception():
    def raise_api_error():
        raise APIError(404, "Not Found")

    def raise_api_error_400():
        raise APIError(400, "Custom")

    with pytest.raises(APIError) as exc_info:
        # raise_api_error()
        raise_api_error_400()

    exception = exc_info.value
    assert exception.code == 404
    assert exception.message == "Not Found"
    # Альтернативная проверка:
    # assert str(exception) == "404: Not Found"

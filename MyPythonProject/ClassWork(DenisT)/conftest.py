import pytest


@pytest.fixture(scope="class")  # Запускается один раз при запуске тестов
def get_token():
    print()
    print("Token generation started...")
    return "test 1234567"

# @pytest.fixture(scope="function")  # Запускается для каждого теста
#
# @pytest.fixture(scope="class")  # Запускается для каждого класса тестов

# @pytest.fixture(scope="session")  # Запускается один раз при запуске тестов
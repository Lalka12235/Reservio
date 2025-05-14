import pytest


@pytest.fixture
def test_user_data():
    return {
        'email': 'user@example.com',
        'username': 'egor',
        'password': 'qwerty',
    }

@pytest.fixture
def test_user_data1():
    return {
        'email': 'user@example.com',
        'username': 'egorchik',
        'password': '123456',
    }

@pytest.fixture
def test_user_data_delete():
    return {
        'username': 'egor',
        'password': 'qwerty',
    }

@pytest.fixture
def test_get_username():
    return 'egor'


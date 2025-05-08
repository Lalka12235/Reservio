import pytest

from app.schemas.user_schema import UserRegisterSchema
from app.services.user_service import UserServices


@pytest.fixture
def test_user_data():
    return {
        'username': 'aspirin',
        'password': 'qwerty',
    }


@pytest.fixture
def created_test_user(test_user_data):
    user_data = UserRegisterSchema(**test_user_data)
    user = UserServices.register_user(user_data)
    yield user
    UserServices.delete_user(test_user_data)
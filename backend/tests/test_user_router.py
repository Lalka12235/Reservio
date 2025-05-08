import pytest
from httpx import AsyncClient, ASGITransport
from main import app
from tests.conftest import test_user_data,created_test_user
from app.schemas.user_schema import UserRegisterSchema
from app.services.user_service import UserServices

class TestUserRouter:
    @pytest.mark.asyncio
    async def test_get_user(test_user_data):
        async with AsyncClient(transport=ASGITransport(app), base_url='http://test') as ac:
            response = await ac.get('/api/v1/users/{username}')
            assert response.status_code == 200
            assert response.json() == {'message': 'User found', 'detail': test_user_data['username']}


    @pytest.mark.asyncio
    async def test_get_user(test_create_data):
        async with AsyncClient(transport=ASGITransport(app), base_url='http://test') as ac:
            response = await ac.post('/api/v1/users/register',json=test_user_data)
            data = response.json()
            await response.status_code == 200
            assert data['username'] == test_user_data['username']
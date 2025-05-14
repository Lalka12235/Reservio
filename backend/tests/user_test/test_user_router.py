import pytest
from httpx import AsyncClient, ASGITransport
from main import app
from tests.user_test.conftest import test_get_username,test_user_data,test_user_data1,test_user_data_delete



class TestUserRouter:
    @pytest.mark.asyncio
    async def test_get_user_success(self, test_get_username: str):
        async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
            response = await ac.get(f'/api/v1/users/{test_get_username}')
            assert response.status_code == 200
            data = response.json()
            assert data['message'] == 'User found'
            assert 'detail' in data
            
    @pytest.mark.asyncio
    async def test_get_user_not_found(self):
        async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
            response = await ac.get('/api/v1/users/nonexistent_user')
            assert response.status_code == 404
            assert response.json() == {'detail': 'User not found'}


    @pytest.mark.asyncio
    async def test_create_user(self,test_user_data1):
        async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
            response = await ac.post('api/v1/users/register',json=test_user_data1)
            data = response.json()
            assert data == {'message': 'Account created', 'user_id': data.get('id')}


    #change api or idk
    @pytest.mark.asyncio
    async def test_delete_user(self,test_user_data_delete,test_get_username: str):
        async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
            response = await ac.delete(f'api/v1/users/{test_get_username}')
            assert response.status_code == 200
            data = response.json()
            print(data)
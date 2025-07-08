import pytest
from httpx import AsyncClient, ASGITransport
from backend.app.main import app
from tests.hotel_test.conftest_hotel import test_hotel_title,test_create_hotel_data



class TestHotelRouter:
    @pytest.mark.asyncio
    async def test_get_hotel_by_title_success(self,test_hotel_title: str ):
        async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
            response = await ac.get(f'/api/v1/hotels/{test_hotel_title}')
            assert response.status_code == 200
            data = response.json()
            assert data == {'message': 'success'}
        
    
    @pytest.mark.asyncio
    async def test_get_hotel_by_title_failed(self):
        async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
            response = await ac.get('/api/v1/hotels/{}')
            assert response.status_code == 404
            data = response.json()
            assert data == {'detail': 'Hotel not found'}
            
    @pytest.mark.asyncio
    async def test_create_hotel(self,test_create_hotel_data):
        async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
            response = await ac.post('/api/v1/hotels/',json=test_create_hotel_data)
            assert response.status_code == 200
            data = response.json()
            assert data == {'message': 'Hotel created successfully','title': data['title'],'description': data['description']}


    @pytest.mark.asyncio
    async def test_delete_hotel(self,test_hotel_title: str):
        async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
            response = await ac.delete(f'/api/v1/hotels/{test_hotel_title}')
            assert response.status_code == 200
            data = response.json()
            assert data == {'message': 'Hotel deleted successfully','title': data['title']}
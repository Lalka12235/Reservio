import pytest
from httpx import AsyncClient, ASGITransport
from backend.app.main import app
from tests.room_test.conftest_room import test_get_room_title
from tests.hotel_test.conftest_hotel import test_hotel_title


class TestRoomRouter:
    @pytest.mark.asyncio
    async def test_get_title_success(self,test_hotel_title: str, test_get_room_title: str):
        async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
            response = await ac.get(f'/api/v1/hotels/{test_hotel_title}/rooms/{test_get_room_title}')
            assert response.status_code == 200
            data = response.json()

    @pytest.mark.asyncio
    async def test_get_title_failed(self, test_get_room_title: str):
        async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
            pass
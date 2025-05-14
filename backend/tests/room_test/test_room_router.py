import pytest
from httpx import AsyncClient, ASGITransport
from main import app
from tests.room_test.conftest_room import test_get_room_title


class TestRoomRouter:
    @pytest.mark.asyncio
    async def test_get_title(self, test_get_room_title: str):
        async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
            response = await ac.get(f'/api/v1/hotels/{...}/rooms/{test_get_room_title}')
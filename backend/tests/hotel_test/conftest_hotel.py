import pytest


@pytest.fixture
def test_hotel_title():
    return 'Hotel Eleon'


@pytest.fixture
def test_create_hotel_data():
    return {
        'title': 'Hotel Eleon',
        'description': 'The best hotel in region',
    }
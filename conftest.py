import pytest

@pytest.fixture
def large_list():
    return [20,18,16,14,12,10,8,6,4,2,0]

@pytest.fixture
def medium_list():
    return [10, 8, 6, 4, 2, 0]

@pytest.fixture
def small_list():
    return [10]

@pytest.fixture
def empty_list():
    return []
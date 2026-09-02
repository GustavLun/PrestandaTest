import pytest
from src.merge_sort import merge_sort
from conftest import medium_list

@pytest.mark.Unit
def test_merge_sort(medium_list): # unit test för att testa att funktionen faktiskt fungerar som den ska.

    result = merge_sort.merge_sort(medium_list)
    expected = sorted(medium_list)

    assert result == expected

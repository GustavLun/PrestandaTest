import pytest

from conftest import medium_list,small_list,empty_list
from src.insertion_sort import insertion_sort


@pytest.mark.Unit
def test_insertion_sort(medium_list):

    result = insertion_sort.insertion_sort(medium_list)

    expected = sorted(medium_list)

    assert result == expected










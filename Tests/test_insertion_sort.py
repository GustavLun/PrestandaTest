import pytest

from conftest import large_list,medium_list,small_list,empty_list
from src.insertion_sort import insertion_sort

@pytest.mark.unit
def test_insertion_sort(medium_list):

    result = insertion_sort.insertion_sort(medium_list)

    expected = sorted(medium_list)

    assert result == expected






# @pytest.mark.Benchmark_insertion
# def test_insertion_sort_large(benchmark, large_list):



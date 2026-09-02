import pytest
from src.insertion_sort import insertion_sort
import random

def large_random_list(size, min_value, max_value):
    return [random.randint( min_value, max_value ) for _ in range(size)]

@pytest.mark.Benchmark_insertion
def test_insertion_sort_large(benchmark):

     benchmark(insertion_sort.insertion_sort,large_random_list(2500,1, 50000))
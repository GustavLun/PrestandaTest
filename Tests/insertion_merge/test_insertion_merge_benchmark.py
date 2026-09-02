import pytest
from src.insertion_sort import insertion_sort
import random

def large_random_list(size, min_value, max_value):
    return [random.randint( min_value, max_value ) for _ in range(size)]

@pytest.mark.Benchmark_insertion
def test_insertion_sort_large(benchmark): #Benchmark test som skall ha ca 100ms runtime.

     benchmark(insertion_sort.insertion_sort,large_random_list(2500,1, 50000))


@pytest.mark.data_collect
def test_insertion_sort_data1(benchmark):  # Benchmarktest där datan samlas som skall användas till ett diagram

    benchmark(insertion_sort.insertion_sort, large_random_list(3000, 1, 50000))

@pytest.mark.data_collect
def test_insertion_sort_data2(benchmark):  # Benchmarktest där datan samlas som skall användas till ett diagram

    benchmark(insertion_sort.insertion_sort, large_random_list(3500, 1, 50000))

@pytest.mark.data_collect
def test_insertion_sort_data3(benchmark):  # Benchmarktest där datan samlas som skall användas till ett diagram

    benchmark(insertion_sort.insertion_sort, large_random_list(4000, 1, 50000))

@pytest.mark.data_collect
def test_insertion_sort_data4(benchmark):  # Benchmarktest där datan samlas som skall användas till ett diagram

    benchmark(insertion_sort.insertion_sort, large_random_list(4500, 1, 50000))
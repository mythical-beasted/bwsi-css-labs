
import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_max_subarray_sum_pos():
	assert max_subarray_sum([1, 2, 3, -2, 5]) == 9

def test_max_subarray_sum_neg():
	assert max_subarray_sum([-1, -2, -3, -4]) == -1
	

def test_max_subarray_sum_non_numeric():
    with pytest.raises(TypeError):
        max_subarray_sum([1, "a", 3])
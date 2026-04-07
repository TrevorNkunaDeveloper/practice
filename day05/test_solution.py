from solution import find_max
import pytest

def test_find_max_largest_num():
    assert(find_max([3,2,6])) == 6

def test_find_max_negative_number():
    assert(find_max([3,2,-6])) == 3   

def test_find_max_array_of_zeros():
    assert(find_max([0,0])) == 0

def test_find_max_single_item():
    assert(find_max([7])) == 7

def test_find_max_empty_list():
    with pytest.raises(ValueError):
        find_max([])
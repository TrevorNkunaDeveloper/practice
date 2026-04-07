from solution import common_elements
import pytest

def test_empty_lists():
    with pytest.raises(ValueError):
        common_elements([],[])

def test_common_elements():
    assert common_elements([1,2,3],[3,4,5,6]) == [3]

def test_no_common_elements():
    assert common_elements([1,2,3],[4,5,6]) == []

def test_common_elements_duplicates_in_lists():
    assert common_elements([1, 1, 2, 3], [1, 1, 3]) == [1, 3]
from solution import count_evens

def test_evens_normal():
    assert count_evens([1,2,3,4,5,6,7,88,945,32]) == 5

def test_no_evens():
    assert count_evens([1,3,5,7]) == 0

def test_all_evens():
    assert count_evens([2,4,6,8]) == 4

def test_empty_list():
    assert count_evens([]) == 0
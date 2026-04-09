from solution import square_numbers

def test_square_numbers_normal():
    assert square_numbers([1,2,3,4]) == [1,4,9,16]

def test_empty_list():
    assert square_numbers([]) == []

def test_negative_numbers():
    assert square_numbers([-1,-2,-3]) == [1,4,9]
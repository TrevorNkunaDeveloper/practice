from solution import max_of_two

def test_max_of_two():
    assert max_of_two(3, 5) == 5
    assert max_of_two(10, 2) == 10
    assert max_of_two(-1, -5) == -1
    assert max_of_two(0, 0) == 0
    
def test_max_of_two_equal():
    assert max_of_two(6, 6) == 6
    assert max_of_two(-3, -3) == -3
    assert max_of_two(0, 0) == 0

def test_max_of_two_negative():
    assert max_of_two(-10, -5) == -5
    assert max_of_two(-1, -2) == -1
    assert max_of_two(-3, -4) == -3


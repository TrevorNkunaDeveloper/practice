from solution import sum_to_n

def test_sum_to_n():
    assert(sum_to_n(4)) == 10

def test_negative_input():
    assert(sum_to_n(-20)) == 0

def test_sum_to_one():
    assert(sum_to_n(1)) == 1

def test_sum_to_zero():
    assert(sum_to_n(0)) == 0
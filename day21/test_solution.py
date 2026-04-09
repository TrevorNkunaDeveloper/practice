from solution import max_profit

def test_max_profit_normal():
    assert max_profit([1,5,2,9,6]) == 8

def test_max_empty_list():
    assert max_profit([]) == 0

def test_no_profit():
    assert max_profit([9,8,7,3,2]) == 0
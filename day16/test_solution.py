from solution import move_zeroes

def test_move_zeroes_normal():
    assert move_zeroes([1,0,2,6,0,9,5]) == [1,2,6,9,5,0,0]

def test_no_zeroes():
    assert move_zeroes([1,2,3,5]) == [1,2,3,5]

def test_all_zeroes():
    assert move_zeroes([0,0,0,0]) == [0,0,0,0]

def test_empty_list():
    assert move_zeroes([]) == []
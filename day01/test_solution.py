from solution import swap_values

def test_swap_two_numbers():
    assert swap_values(6,4) == [4,6]

def test_swap_strings():
    assert swap_values("t","8") == ["8","t"]

def test_swap_string_and_int():
    assert swap_values("t", 8) ==[8,"t"]


def test_swap_same_values():
    assert swap_values(1,1) ==[1,1]
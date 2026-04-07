from solution import two_sum 

def test_two_sum():
    assert(two_sum([1,8,6,3],9)) == [0,1]

def test_duplicates():
    assert(two_sum([3,3],6)) ==[0,1]
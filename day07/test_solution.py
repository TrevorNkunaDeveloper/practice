from solution import remove_duplicates

def test_remove_duplicates():
    assert(remove_duplicates([1,2,2,3,1,4])) == [1,2,3,4]

def test_remove_no_duplicates():
    assert(remove_duplicates([1,2,3])) == [1,2,3]

def test_empty_list():
    assert(remove_duplicates([])) == []

def test_all_same():
    assert(remove_duplicates([6,6,6,])) == [6]
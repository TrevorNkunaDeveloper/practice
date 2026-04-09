from solution import sort_by_length

def test_sort_by_length_normal():
    assert sort_by_length(["apple", "kiwi", "banana"]) == ["kiwi", "apple", "banana"]

def test_empty_list():
    assert sort_by_length([]) == []
    
def test_same_length_words():
    assert sort_by_length(["bat", "cat", "dog"]) == ["bat", "cat", "dog"]
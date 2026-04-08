from solution import word_frequency

def test_word_frequency_normal():
    assert word_frequency("This is a normal sentance") == {'this': 1,'is': 1,'a': 1,'normal':1,'sentance':1,}

def test_empty_sentance():
    assert word_frequency("") == {}

def test_one_word_sentance():
    assert word_frequency("Hello") == {'hello':1}


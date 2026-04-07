from solution import is_palindrome

def test_palidrome_true():
    assert(is_palindrome("level")) == True

def test_palindrome_false():
    assert(is_palindrome("Random String")) == False

def test_palindrome_single_character():
    assert(is_palindrome("n")) == True

def test_palindrome_empty_character():
    assert(is_palindrome("")) == True
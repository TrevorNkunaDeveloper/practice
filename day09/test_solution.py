from solution import longest_word
import pytest
def test_longest_word():
    assert(longest_word(["Longest","Word","List"])) == "Longest"
    assert(longest_word(["my","python","Umbrella"])) == "Umbrella"

def test_return_first_if_equal():
    assert(longest_word(["mouse","keyboard","computer"])) == "keyboard"    


def test_empty_list():
    with pytest.raises(ValueError):
        longest_word([])

def test_single_word_list():
    assert(longest_word(["Single"])) == "Single"


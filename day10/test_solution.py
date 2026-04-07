from solution import char_frequency
import pytest
def test_banana_counts():
    assert char_frequency("banana") == {"b": 1, "a": 3, "n": 2}

def test_empty_string():
    with pytest.raises(ValueError):
        char_frequency("")

def test_single_character():
    assert char_frequency("a") == {"a": 1}

def test_spaces_counted():
    assert char_frequency("a a") == {"a": 2, " ": 1}
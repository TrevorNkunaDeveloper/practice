from solution import even_or_odd

def test_even():
    assert(even_or_odd(2)) == "even"

def test_odd():
    assert(even_or_odd(3)) == "odd"

def test_divide_by_zero():
    assert(even_or_odd(0)) == "even"

def test_divide_by_negavite():
    assert(even_or_odd(-4)) == "even"
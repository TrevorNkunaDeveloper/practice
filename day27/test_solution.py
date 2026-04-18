from solution import binary_search
def test_target_found():
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
def test_target_not_found():
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
def test_single_item_found():
    assert binary_search([5], 5) == 0
def test_empty_list():
    assert binary_search([], 1) == -1
from solution import get_student_mark

def test_student_exists():
    assert get_student_mark({"Tom": 70, "Sara": 85}, "Sara") == 85

def test_student_missing():
    assert get_student_mark({"Tom": 70}, "Mike") == "Not found"
    
def test_empty_records():
    assert get_student_mark({}, "Tom") == "Not found"
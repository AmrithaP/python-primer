import functions
from buggy import multiply
    
def test_sum():
    assert sum([1, 2, 3]) == 6

def test_add_numbers():
    assert functions.add_numbers(2, 3) == 5
    assert functions.add_numbers(-1, 1) == 0

def test_is_even():
    assert functions.is_even(4) is True
    assert functions.is_even(5) is False
    assert functions.is_even(0) is True

def test_reverse_string():
    assert functions.reverse_string("hello") == "olleh"
    assert functions.reverse_string("") == ""
    assert functions.reverse_string("a") == "a"

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6
    assert multiply(1.5, 2) == 3.0

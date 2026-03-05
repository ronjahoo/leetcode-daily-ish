from solution import (
    validParanthesesFirst,
    validParanthesesSecond,
)

def test_simple_round_first():
    assert validParanthesesFirst("()") == True

def test_simple_round_second():
    assert validParanthesesSecond("()") == True

def test_multiple_types_first():
    assert validParanthesesFirst("()[]{}") == True

def test_multiple_types_second():
    assert validParanthesesSecond("()[]{}") == True

def test_mismatched_first():
    assert validParanthesesFirst("(]") == False

def test_mismatched_second():
    assert validParanthesesSecond("(]") == False

def test_nested_first():
    assert validParanthesesFirst("([])") == True

def test_nested_second():
    assert validParanthesesSecond("([])") == True

def test_wrong_order_first():
    assert validParanthesesFirst("([)]") == False

def test_wrong_order_second():
    assert validParanthesesSecond("([)]") == False

def test_only_open_first():
    assert validParanthesesFirst("(((") == False

def test_only_open_second():
    assert validParanthesesSecond("(((") == False

def test_only_close_first():
    assert validParanthesesFirst(")))") == False

def test_only_close_second():
    assert validParanthesesSecond(")))") == False

def test_deeply_nested_first():
    assert validParanthesesFirst("({[]})") == True

def test_deeply_nested_second():
    assert validParanthesesSecond("({[]})") == True

def test_single_open_first():
    assert validParanthesesFirst("(") == False

def test_single_open_second():
    assert validParanthesesSecond("(") == False

def test_single_close_first():
    assert validParanthesesFirst(")") == False

def test_single_close_second():
    assert validParanthesesSecond(")") == False

def test_long_valid_first():
    assert validParanthesesFirst("()()()[][]{}{}") == True

def test_long_valid_second():
    assert validParanthesesSecond("()()()[][]{}{}") == True

def test_long_invalid_first():
    assert validParanthesesFirst("()()()[]{}{") == False

def test_long_invalid_second():
    assert validParanthesesSecond("()()()[]{}{") == False
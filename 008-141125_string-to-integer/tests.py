from solution import (
    myAtoiFirst,
    myAtoiSecond,
)

def test_example1_simple_positive_first():
    s = "42"
    assert myAtoiFirst(s) == 42

def test_example1_simple_positive_second():
    s = "42"
    assert myAtoiSecond(s) == 42

def test_example2_negative_with_spaces_first():
    s = "   -042"
    assert myAtoiFirst(s) == -42

def test_example2_negative_with_spaces_second():
    s = "   -042"
    assert myAtoiSecond(s) == -42

def test_example3_stops_at_nondigit_first():
    s = "1337c0d3"
    assert myAtoiFirst(s) == 1337

def test_example3_stops_at_nondigit_second():
    s = "1337c0d3"
    assert myAtoiSecond(s) == 1337

def test_example4_zero_then_minus_first():
    s = "0-1"
    assert myAtoiFirst(s) == 0

def test_example4_zero_then_minus_second():
    s = "0-1"
    assert myAtoiSecond(s) == 0

def test_example5_starts_with_words_first():
    s = "words and 987"
    assert myAtoiFirst(s) == 0

def test_example5_starts_with_words_second():
    s = "words and 987"
    assert myAtoiSecond(s) == 0

def test_only_spaces_first():
    s = "     "
    assert myAtoiFirst(s) == 0

def test_only_spaces_second():
    s = "     "
    assert myAtoiSecond(s) == 0

def test_plus_sign_only_first():
    s = "+"
    assert myAtoiFirst(s) == 0

def test_plus_sign_only_second():
    s = "+"
    assert myAtoiSecond(s) == 0

def test_minus_sign_only_first():
    s = "-"
    assert myAtoiFirst(s) == 0

def test_minus_sign_only_second():
    s = "-"
    assert myAtoiSecond(s) == 0

def test_overflow_positive_first():
    s = "91283472332"
    assert myAtoiFirst(s) == 2147483647

def test_overflow_positive_second():
    s = "91283472332"
    assert myAtoiSecond(s) == 2147483647

def test_overflow_negative_first():
    s = "-91283472332"
    assert myAtoiFirst(s) == -2147483648

def test_overflow_negative_second():
    s = "-91283472332"
    assert myAtoiSecond(s) == -2147483648

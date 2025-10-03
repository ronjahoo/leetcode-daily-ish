from solution import (
    zigzagFirst,
    zigzagSecond
)

def test_example1_zigzagFirst():
    s, n = "PAYPALISHIRING", 3
    assert zigzagFirst(s, n) == "PAHNAPLSIIGYIR"

def test_example1_zigzagSecond():
    s, n = "PAYPALISHIRING", 3
    assert zigzagSecond(s, n) == "PAHNAPLSIIGYIR"

def test_example2_zigzagFirst():
    s, n = "PAYPALISHIRING", 4
    assert zigzagFirst(s, n) == "PINALSIGYAHRPI"

def test_example2_zigzagSecond():
    s, n = "PAYPALISHIRING", 4
    assert zigzagSecond(s, n) == "PINALSIGYAHRPI"

def test_example3_zigzagFirst():
    s, n = "A", 1
    assert zigzagFirst(s, n) == "A"

def test_example3_zigzagSecond():
    s, n = "A", 1
    assert zigzagSecond(s, n) == "A"

def test_numrows_ge_len_zigzagFirst():
    s, n = "AB", 4  
    assert zigzagFirst(s, n) == "AB"

def test_numrows_ge_len_zigzagSecond():
    s, n = "AB", 4
    assert zigzagSecond(s, n) == "AB"

def test_numrows_is_one_zigzagFirst():
    s, n = "HELLO", 1
    assert zigzagFirst(s, n) == "HELLO"

def test_numrows_is_one_zigzagSecond():
    s, n = "HELLO", 1
    assert zigzagSecond(s, n) == "HELLO"

def test_two_rows_example_zigzagFirst():
    s, n = "PAYPALISHIRING", 2
    assert zigzagFirst(s, n) == "PYAIHRNAPLSIIG"

def test_two_rows_example_zigzagSecond():
    s, n = "PAYPALISHIRING", 2
    assert zigzagSecond(s, n) == "PYAIHRNAPLSIIG"

def test_short_mixed_zigzagFirst():
    s, n = "ABCDE", 4
    assert zigzagFirst(s, n) == "ABCED"

def test_short_mixed_zigzagSecond():
    s, n = "ABCDE", 4
    assert zigzagSecond(s, n) == "ABCED"

def test_punctuation_zigzagFirst():
    s, n = "A,B.C", 3
    assert zigzagFirst(s, n) == "AC,.B"

def test_punctuation_zigzagSecond():
    s, n = "A,B.C", 3
    assert zigzagSecond(s, n) == "AC,.B"
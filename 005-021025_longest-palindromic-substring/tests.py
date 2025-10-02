import pytest
from solution import (
    palindromeFromHeads,
    palindromeFromCenter,
)

def test_example1_expand():
    s = "babad"
    res = palindromeFromCenter(s)
    # LeetCode sallii "bab" TAI "aba"
    assert res in {"bab", "aba"}

def test_example1_dp():
    s = "babad"
    res = palindromeFromHeads(s)
    assert res in {"bab", "aba"}

def test_example2_expand():
    s = "cbbd"
    assert palindromeFromCenter(s) == "bb"

def test_example2_dp():
    s = "cbbd"
    assert palindromeFromHeads(s) == "bb"

def test_empty_expand():
    s = ""
    assert palindromeFromCenter(s) == ""

def test_empty_dp():
    s = ""
    assert palindromeFromHeads(s) == ""

def test_single_char_expand():
    s = "a"
    assert palindromeFromCenter(s) == "a"

def test_single_char_dp():
    s = "a"
    assert palindromeFromHeads(s) == "a"

def test_all_same_expand():
    s = "aaaa"
    assert palindromeFromCenter(s) == "aaaa"

def test_all_same_dp():
    s = "aaaa"
    assert palindromeFromHeads(s) == "aaaa"

def test_no_longer_than_one_expand():
    s = "abcd"
    res = palindromeFromCenter(s)
    assert len(res) == 1
    assert res in set(s)

def test_no_longer_than_one_dp():
    s = "abcd"
    res = palindromeFromHeads(s)
    assert len(res) == 1
    assert res in set(s)

def test_even_length_palindrome_expand():
    s = "abccba"
    assert palindromeFromCenter(s) == "abccba"

def test_even_length_palindrome_dp():
    s = "abccba"
    assert palindromeFromHeads(s) == "abccba"

def test_mixed_internal_expand():
    s = "forgeeksskeegfor"
    # pisin on "geeksskeeg"
    assert palindromeFromCenter(s) == "geeksskeeg"

def test_mixed_internal_dp():
    s = "forgeeksskeegfor"
    assert palindromeFromHeads(s) == "geeksskeeg"

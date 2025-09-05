import pytest
from solution import (
    length_of_longest_substring_hash,
    length_of_longest_substring_dict,
)

def test_example1_hash():
    assert length_of_longest_substring_hash("abcabcbb") == 3

def test_example2_hash():
    assert length_of_longest_substring_hash("bbbbb") == 1

def test_example3_hash():
    assert length_of_longest_substring_hash("pwwkew") == 3

def test_example1_dict():
    assert length_of_longest_substring_dict("abcabcbb") == 3

def test_example2_dict():
    assert length_of_longest_substring_dict("bbbbb") == 1

def test_example3_dict():
    assert length_of_longest_substring_dict("pwwkew") == 3

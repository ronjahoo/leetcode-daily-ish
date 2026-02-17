from solution import (
    threeSumClosestFirst,
    threeSumClosestSecond,
)

def test_example1_first():
    assert threeSumClosestFirst([-1, 2, 1, -4], 1) == 2

def test_example1_second():
    assert threeSumClosestSecond([-1, 2, 1, -4], 1) == 2

def test_example2_first():
    assert threeSumClosestFirst([0, 0, 0], 1) == 0

def test_example2_second():
    assert threeSumClosestSecond([0, 0, 0], 1) == 0

def test_exact_match_first():
    assert threeSumClosestFirst([1, 1, 1, 0], -100) == 2

def test_exact_match_second():
    assert threeSumClosestSecond([1, 1, 1, 0], -100) == 2

def test_negative_target_first():
    assert threeSumClosestFirst([-3, -2, -5, 3, -4], -1) == -2

def test_negative_target_second():
    assert threeSumClosestSecond([-3, -2, -5, 3, -4], -1) == -2

def test_large_numbers_first():
    assert threeSumClosestFirst([1000, -1000, 2000, -2000, 3], 1) == 3

def test_large_numbers_second():
    assert threeSumClosestSecond([1000, -1000, 2000, -2000, 3], 1) == 3

def test_minimum_valid_length_first():
    assert threeSumClosestFirst([1, 2, 3], 10) == 6

def test_minimum_valid_length_second():
    assert threeSumClosestSecond([1, 2, 3], 10) == 6

def test_all_negative_first():
    assert threeSumClosestFirst([-8, -6, -5, -3], -7) == -14

def test_all_negative_second():
    assert threeSumClosestSecond([-8, -6, -5, -3], -7) == -14

def test_duplicates_first():
    assert threeSumClosestFirst([1, 1, 1, 1], 0) == 3

def test_duplicates_second():
    assert threeSumClosestSecond([1, 1, 1, 1], 0) == 3

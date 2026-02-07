from solution import (
    maxAreaFirst,
    maxAreaSecond,
)

def test_example1_first():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert maxAreaFirst(height) == 49

def test_example1_second():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert maxAreaSecond(height) == 49

def test_example2_first():
    height = [1, 1]
    assert maxAreaFirst(height) == 1

def test_example2_second():
    height = [1, 1]
    assert maxAreaSecond(height) == 1

def test_min_case_two_bars_first():
    height = [2, 3]
    assert maxAreaFirst(height) == 2  

def test_min_case_two_bars_second():
    height = [2, 3]
    assert maxAreaSecond(height) == 2

def test_all_zeros_first():
    height = [0, 0, 0, 0]
    assert maxAreaFirst(height) == 0

def test_all_zeros_second():
    height = [0, 0, 0, 0]
    assert maxAreaSecond(height) == 0

def test_all_equal_first():
    height = [5, 5, 5, 5, 5]
    assert maxAreaFirst(height) == 20  

def test_all_equal_second():
    height = [5, 5, 5, 5, 5]
    assert maxAreaSecond(height) == 20

def test_strictly_increasing_first():
    height = [1, 2, 3, 4, 5]
    assert maxAreaFirst(height) == 6  

def test_strictly_increasing_second():
    height = [1, 2, 3, 4, 5]
    assert maxAreaSecond(height) == 6

def test_strictly_decreasing_first():
    height = [5, 4, 3, 2, 1]
    assert maxAreaFirst(height) == 6  

def test_strictly_decreasing_second():
    height = [5, 4, 3, 2, 1]
    assert maxAreaSecond(height) == 6

def test_max_at_ends_first():
    height = [9, 1, 1, 1, 9]
    assert maxAreaFirst(height) == 36  

def test_max_at_ends_second():
    height = [9, 1, 1, 1, 9]
    assert maxAreaSecond(height) == 36

def test_tall_in_middle_not_best_first():
    height = [1, 100, 1, 1, 1]
    assert maxAreaFirst(height) == 4

def test_tall_in_middle_not_best_second():
    height = [1, 100, 1, 1, 1]
    assert maxAreaSecond(height) == 4

def test_plateau_then_drop_first():
    height = [4, 4, 4, 1, 1]
    assert maxAreaFirst(height) == 8  

def test_plateau_then_drop_second():
    height = [4, 4, 4, 1, 1]
    assert maxAreaSecond(height) == 8

def test_spikes_first():
    height = [1, 3, 2, 5, 25, 24, 5]
    assert maxAreaFirst(height) == 24  

def test_spikes_second():
    height = [1, 3, 2, 5, 25, 24, 5]
    assert maxAreaSecond(height) == 24

def test_single_tall_far_apart_first():
    height = [1000, 1, 1, 1, 1000]
    assert maxAreaFirst(height) == 4000  

def test_single_tall_far_apart_second():
    height = [1000, 1, 1, 1, 1000]
    assert maxAreaSecond(height) == 4000


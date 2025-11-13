from solution import (
    reverse_first_version,
    reverse_second_version
)

def test_example1_reverse_first():
    x = 123
    assert reverse_first_version(x) == 321

def test_example1_reverse_second():
    x = 123
    assert reverse_second_version(x) == 321

def test_example2_reverse_first():
    x = -123
    assert reverse_first_version(x) == -321

def test_example2_reverse_second():
    x = -123
    assert reverse_second_version(x) == -321

def test_example3_reverse_first():
    x = 120
    assert reverse_first_version(x) == 21

def test_example3_reverse_second():
    x = 120
    assert reverse_second_version(x) == 21

def test_zero_first():
    x = 0
    assert reverse_first_version(x) == 0

def test_zero_second():
    x = 0
    assert reverse_second_version(x) == 0

def test_single_digit_first():
    x = 7
    assert reverse_first_version(x) == 7

def test_single_digit_second():
    x = 7
    assert reverse_second_version(x) == 7

def test_negative_single_digit_first():
    x = -8
    assert reverse_first_version(x) == -8

def test_negative_single_digit_second():
    x = -8
    assert reverse_second_version(x) == -8

def test_leading_zero_output_first():
    x = 1000  
    assert reverse_first_version(x) == 1

def test_leading_zero_output_second():
    x = 1000
    assert reverse_second_version(x) == 1

def test_overflow_first():
    x = 1534236469  
    assert reverse_first_version(x) == 0

def test_overflow_second():
    x = 1534236469
    assert reverse_second_version(x) == 0

def test_negative_overflow_first():
    x = -1563847412  
    assert reverse_first_version(x) == 0

def test_negative_overflow_second():
    x = -1563847412
    assert reverse_second_version(x) == 0

def test_max_edge_first():
    x = 1463847412  
    assert reverse_first_version(x) == 2147483641

def test_max_edge_second():
    x = 1463847412
    assert reverse_second_version(x) == 2147483641

def test_max_overlimit_first():
    x = 1563847412  
    assert reverse_first_version(x) == 0

def test_max_overlimit_second():
    x = 1563847412
    assert reverse_second_version(x) == 0

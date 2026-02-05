from solution import (
    palindromeNumberFirst,
    palindromeNumberSecond,
)

def test_example1_true_first():
    n = 121
    assert palindromeNumberFirst(n) is True

def test_example1_true_second():
    n = 121
    assert palindromeNumberSecond(n) is True

def test_example2_false_negative_first():
    n = -121
    assert palindromeNumberFirst(n) is False

def test_example2_false_negative_second():
    n = -121
    assert palindromeNumberSecond(n) is False

def test_example3_false_trailing_zero_first():
    n = 10
    assert palindromeNumberFirst(n) is False

def test_example3_false_trailing_zero_second():
    n = 10
    assert palindromeNumberSecond(n) is False

def test_zero_first():
    n = 0
    assert palindromeNumberFirst(n) is True

def test_zero_second():
    n = 0
    assert palindromeNumberSecond(n) is True

def test_single_digit_first():
    n = 7
    assert palindromeNumberFirst(n) is True

def test_single_digit_second():
    n = 7
    assert palindromeNumberSecond(n) is True

def test_even_length_palindrome_first():
    n = 1221
    assert palindromeNumberFirst(n) is True

def test_even_length_palindrome_second():
    n = 1221
    assert palindromeNumberSecond(n) is True

def test_even_length_not_palindrome_first():
    n = 1231
    assert palindromeNumberFirst(n) is False

def test_even_length_not_palindrome_second():
    n = 1231
    assert palindromeNumberSecond(n) is False

def test_odd_length_palindrome_first():
    n = 12321
    assert palindromeNumberFirst(n) is True

def test_odd_length_palindrome_second():
    n = 12321
    assert palindromeNumberSecond(n) is True

def test_odd_length_not_palindrome_first():
    n = 12341
    assert palindromeNumberFirst(n) is False

def test_odd_length_not_palindrome_second():
    n = 12341
    assert palindromeNumberSecond(n) is False

def test_repeated_digits_palindrome_first():
    n = 111111
    assert palindromeNumberFirst(n) is True

def test_repeated_digits_palindrome_second():
    n = 111111
    assert palindromeNumberSecond(n) is True

def test_large_palindrome_first():
    n = 123456789987654321
    assert palindromeNumberFirst(n) is True

def test_large_palindrome_second():
    n = 123456789987654321
    assert palindromeNumberSecond(n) is True

def test_large_not_palindrome_first():
    n = 123456789987654320
    assert palindromeNumberFirst(n) is False

def test_large_not_palindrome_second():
    n = 123456789987654320
    assert palindromeNumberSecond(n) is False

def test_middle_mismatch_first():
    n = 10021
    assert palindromeNumberFirst(n) is False

def test_middle_mismatch_second():
    n = 10021
    assert palindromeNumberSecond(n) is False

def test_palindrome_with_zeros_inside_first():
    n = 1001
    assert palindromeNumberFirst(n) is True

def test_palindrome_with_zeros_inside_second():
    n = 1001
    assert palindromeNumberSecond(n) is True
from solution import (
    regExMatchFirst,
    regExMatchSecond,
)

def test_exact_match_first():
    assert regExMatchFirst("abc", "abc") is True

def test_exact_match_second():
    assert regExMatchSecond("abc", "abc") is True

def test_dot_single_char_first():
    assert regExMatchFirst("abc", "a.c") is True

def test_dot_single_char_second():
    assert regExMatchSecond("abc", "a.c") is True

def test_dot_no_match_first():
    assert regExMatchFirst("abc", "a.d") is False

def test_dot_no_match_second():
    assert regExMatchSecond("abc", "a.d") is False

def test_star_zero_occurrences_first():
    assert regExMatchFirst("b", "a*b") is True

def test_star_zero_occurrences_second():
    assert regExMatchSecond("b", "a*b") is True

def test_star_multiple_occurrences_first():
    assert regExMatchFirst("aaab", "a*b") is True

def test_star_multiple_occurrences_second():
    assert regExMatchSecond("aaab", "a*b") is True

def test_star_no_match_first():
    assert regExMatchFirst("ab", "a*c") is False

def test_star_no_match_second():
    assert regExMatchSecond("ab", "a*c") is False

def test_dot_star_match_all_first():
    assert regExMatchFirst("anything", ".*") is True

def test_dot_star_match_all_second():
    assert regExMatchSecond("anything", ".*") is True

def test_dot_star_partial_first():
    assert regExMatchFirst("ab", ".*c") is False

def test_dot_star_partial_second():
    assert regExMatchSecond("ab", ".*c") is False

def test_leetcode_case1_first():
    assert regExMatchFirst("aa", "a") is False

def test_leetcode_case1_second():
    assert regExMatchSecond("aa", "a") is False

def test_leetcode_case2_first():
    assert regExMatchFirst("aa", "a*") is True

def test_leetcode_case2_second():
    assert regExMatchSecond("aa", "a*") is True

def test_leetcode_case3_first():
    assert regExMatchFirst("ab", ".*") is True

def test_leetcode_case3_second():
    assert regExMatchSecond("ab", ".*") is True

def test_leetcode_case4_first():
    assert regExMatchFirst("aab", "c*a*b") is True

def test_leetcode_case4_second():
    assert regExMatchSecond("aab", "c*a*b") is True

def test_leetcode_case5_first():
    assert regExMatchFirst("mississippi", "mis*is*p*.") is False

def test_leetcode_case5_second():
    assert regExMatchSecond("mississippi", "mis*is*p*.") is False

def test_empty_string_and_pattern_first():
    assert regExMatchFirst("", "") is True

def test_empty_string_and_pattern_second():
    assert regExMatchSecond("", "") is True

def test_empty_string_with_star_pattern_first():
    assert regExMatchFirst("", "a*b*c*") is True

def test_empty_string_with_star_pattern_second():
    assert regExMatchSecond("", "a*b*c*") is True

def test_nonempty_string_empty_pattern_first():
    assert regExMatchFirst("abc", "") is False

def test_nonempty_string_empty_pattern_second():
    assert regExMatchSecond("abc", "") is False

from solution import (
    longestCommonPrefix,
    longestCommonPrefixSecond,
)

def test_example1_first():
    assert longestCommonPrefix(["flower","flow","flight"]) == "fl"

def test_example1_second():
    assert longestCommonPrefixSecond(["flower","flow","flight"]) == "fl"


def test_example2_first():
    assert longestCommonPrefix(["dog","racecar","car"]) == ""

def test_example2_second():
    assert longestCommonPrefixSecond(["dog","racecar","car"]) == ""

def test_empty_list_first():
    assert longestCommonPrefix([]) == ""

def test_empty_list_second():
    assert longestCommonPrefixSecond([]) == ""


def test_contains_empty_string_first():
    assert longestCommonPrefix(["", "abc", "abcd"]) == ""

def test_contains_empty_string_second():
    assert longestCommonPrefixSecond(["", "abc", "abcd"]) == ""

def test_single_string_first():
    assert longestCommonPrefix(["quantum"]) == "quantum"

def test_single_string_second():
    assert longestCommonPrefixSecond(["quantum"]) == "quantum"

def test_full_match_first():
    assert longestCommonPrefix(["test", "test", "test"]) == "test"

def test_full_match_second():
    assert longestCommonPrefixSecond(["test", "test", "test"]) == "test"

def test_partial_match_first():
    assert longestCommonPrefix(["interspecies","interstellar","interstate"]) == "inters"

def test_partial_match_second():
    assert longestCommonPrefixSecond(["interspecies","interstellar","interstate"]) == "inters"

def test_no_common_prefix_first():
    assert longestCommonPrefix(["a","b","c"]) == ""

def test_no_common_prefix_second():
    assert longestCommonPrefixSecond(["a","b","c"]) == ""

def test_shortest_is_prefix_first():
    assert longestCommonPrefix(["flow","flower","flown"]) == "flow"

def test_shortest_is_prefix_second():
    assert longestCommonPrefixSecond(["flow","flower","flown"]) == "flow"
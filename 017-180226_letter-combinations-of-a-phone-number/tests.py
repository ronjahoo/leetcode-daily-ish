from solution import (
    letterCombinationsFirst,
    letterCombinationsSecond,
)


def test_example1_first():
    result = sorted(letterCombinationsFirst("23"))
    assert result == sorted(["ad","ae","af","bd","be","bf","cd","ce","cf"])


def test_example1_second():
    result = sorted(letterCombinationsSecond("23"))
    assert result == sorted(["ad","ae","af","bd","be","bf","cd","ce","cf"])


def test_single_digit_first():
    assert sorted(letterCombinationsFirst("2")) == ["a", "b", "c"]


def test_single_digit_second():
    assert sorted(letterCombinationsSecond("2")) == ["a", "b", "c"]


def test_empty_input_first():
    assert letterCombinationsFirst("") == []


def test_empty_input_second():
    assert letterCombinationsSecond("") == []


def test_multiple_digits_first():
    result = letterCombinationsFirst("79")
    assert len(result) == 16  # 4 * 4


def test_multiple_digits_second():
    result = letterCombinationsSecond("79")
    assert len(result) == 16


def test_max_length_first():
    result = letterCombinationsFirst("2345")
    assert len(result) == 3 * 3 * 3 * 3  # 81


def test_max_length_second():
    result = letterCombinationsSecond("2345")
    assert len(result) == 3 * 3 * 3 * 3

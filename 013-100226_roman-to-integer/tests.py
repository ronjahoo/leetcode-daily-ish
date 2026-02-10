from solution import (
    romanToIntFirst,
    romanToIntSecond,
)

def test_example1_first():
    assert romanToIntFirst("III") == 3

def test_example1_second():
    assert romanToIntSecond("III") == 3

def test_example2_first():
    assert romanToIntFirst("LVIII") == 58

def test_example2_second():
    assert romanToIntSecond("LVIII") == 58

def test_example3_first():
    assert romanToIntFirst("MCMXCIV") == 1994

def test_example3_second():
    assert romanToIntSecond("MCMXCIV") == 1994

def test_min_value_first():
    assert romanToIntFirst("I") == 1

def test_min_value_second():
    assert romanToIntSecond("I") == 1

def test_max_standard_value_first():
    assert romanToIntFirst("MMMCMXCIX") == 3999

def test_max_standard_value_second():
    assert romanToIntSecond("MMMCMXCIX") == 3999

def test_repeated_symbols_first():
    assert romanToIntFirst("XXX") == 30

def test_repeated_symbols_second():
    assert romanToIntSecond("XXX") == 30

def test_subtractive_notation_4_first():
    assert romanToIntFirst("IV") == 4

def test_subtractive_notation_4_second():
    assert romanToIntSecond("IV") == 4

def test_subtractive_notation_9_first():
    assert romanToIntFirst("IX") == 9

def test_subtractive_notation_9_second():
    assert romanToIntSecond("IX") == 9

def test_mixed_places_first():
    assert romanToIntFirst("CMXLIV") == 944

def test_mixed_places_second():
    assert romanToIntSecond("CMXLIV") == 944

def test_round_hundreds_first():
    assert romanToIntFirst("CCC") == 300

def test_round_hundreds_second():
    assert romanToIntSecond("CCC") == 300

def test_round_thousands_first():
    assert romanToIntFirst("MM") == 2000

def test_round_thousands_second():
    assert romanToIntSecond("MM") == 2000

def test_tricky_given_case_first():
    assert romanToIntFirst("MMMDXXXVI") == 3536

def test_tricky_given_case_second():
    assert romanToIntSecond("MMMDXXXVI") == 3536

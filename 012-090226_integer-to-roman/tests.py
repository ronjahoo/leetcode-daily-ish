from solution import (
    intToRomanFirst,
    intToRomanSecond,
)

def test_example1_first():
    assert intToRomanFirst(3) == "III"

def test_example1_second():
    assert intToRomanSecond(3) == "III"

def test_example2_first():
    assert intToRomanFirst(58) == "LVIII"

def test_example2_second():
    assert intToRomanSecond(58) == "LVIII"

def test_example3_first():
    assert intToRomanFirst(1994) == "MCMXCIV"

def test_example3_second():
    assert intToRomanSecond(1994) == "MCMXCIV"

def test_min_value_first():
    assert intToRomanFirst(1) == "I"

def test_min_value_second():
    assert intToRomanSecond(1) == "I"

def test_max_standard_value_first():
    assert intToRomanFirst(3999) == "MMMCMXCIX"

def test_max_standard_value_second():
    assert intToRomanSecond(3999) == "MMMCMXCIX"

def test_repeated_symbols_first():
    assert intToRomanFirst(30) == "XXX"

def test_repeated_symbols_second():
    assert intToRomanSecond(30) == "XXX"

def test_subtractive_notation_4_first():
    assert intToRomanFirst(4) == "IV"

def test_subtractive_notation_4_second():
    assert intToRomanSecond(4) == "IV"

def test_subtractive_notation_9_first():
    assert intToRomanFirst(9) == "IX"

def test_subtractive_notation_9_second():
    assert intToRomanSecond(9) == "IX"

def test_mixed_places_first():
    assert intToRomanFirst(944) == "CMXLIV"

def test_mixed_places_second():
    assert intToRomanSecond(944) == "CMXLIV"

def test_round_hundreds_first():
    assert intToRomanFirst(300) == "CCC"

def test_round_hundreds_second():
    assert intToRomanSecond(300) == "CCC"

def test_round_thousands_first():
    assert intToRomanFirst(2000) == "MM"

def test_round_thousands_second():
    assert intToRomanSecond(2000) == "MM"

from solution import (
    generateParanthesesFirst,
    generateParanthesesSecond,
)

def test_example1_first():
    assert sorted(generateParanthesesFirst(3)) == sorted(["((()))","(()())","(())()","()(())","()()()"])

def test_example1_second():
    assert sorted(generateParanthesesSecond(3)) == sorted(["((()))","(()())","(())()","()(())","()()()"])

def test_n1_first():
    assert generateParanthesesFirst(1) == ["()"]

def test_n1_second():
    assert generateParanthesesSecond(1) == ["()"]

def test_n2_first():
    assert sorted(generateParanthesesFirst(2)) == sorted(["(())", "()()"])

def test_n2_second():
    assert sorted(generateParanthesesSecond(2)) == sorted(["(())", "()()"])

def test_count_n3_first():
    assert len(generateParanthesesFirst(3)) == 5

def test_count_n3_second():
    assert len(generateParanthesesSecond(3)) == 5

def test_count_n4_first():
    assert len(generateParanthesesFirst(4)) == 14

def test_count_n4_second():
    assert len(generateParanthesesSecond(4)) == 14

def test_count_n5_first():
    assert len(generateParanthesesFirst(5)) == 42

def test_count_n5_second():
    assert len(generateParanthesesSecond(5)) == 42

def test_all_valid_first():
    def is_valid(s):
        count = 0
        for c in s:
            if c == "(": count += 1
            else: count -= 1
            if count < 0: return False
        return count == 0
    assert all(is_valid(s) for s in generateParanthesesFirst(4))

def test_all_valid_second():
    def is_valid(s):
        count = 0
        for c in s:
            if c == "(": count += 1
            else: count -= 1
            if count < 0: return False
        return count == 0
    assert all(is_valid(s) for s in generateParanthesesSecond(4))

def test_no_duplicates_first():
    result = generateParanthesesFirst(4)
    assert len(result) == len(set(result))

def test_no_duplicates_second():
    result = generateParanthesesSecond(4)
    assert len(result) == len(set(result))

def test_correct_length_first():
    assert all(len(s) == 6 for s in generateParanthesesFirst(3))

def test_correct_length_second():
    assert all(len(s) == 6 for s in generateParanthesesSecond(3))

def test_n8_count_first():
    assert len(generateParanthesesFirst(8)) == 1430

def test_n8_count_second():
    assert len(generateParanthesesSecond(8)) == 1430

def test_both_agree():
    for n in range(1, 6):
        assert sorted(generateParanthesesFirst(n)) == sorted(generateParanthesesSecond(n))
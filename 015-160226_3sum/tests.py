from solution import (
    threeSumFirst,
    threeSumSecond,
)

def normalize(output):
    return sorted([sorted(triplet) for triplet in output])

def test_example1_first():
    assert normalize(threeSumFirst([-1,0,1,2,-1,-4])) == normalize([[-1,-1,2],[-1,0,1]])

def test_example1_second():
    assert normalize(threeSumSecond([-1,0,1,2,-1,-4])) == normalize([[-1,-1,2],[-1,0,1]])

def test_example2_first():
    assert normalize(threeSumFirst([0,1,1])) == []

def test_example2_second():
    assert normalize(threeSumSecond([0,1,1])) == []

def test_example3_first():
    assert normalize(threeSumFirst([0,0,0])) == [[0,0,0]]

def test_example3_second():
    assert normalize(threeSumSecond([0,0,0])) == [[0,0,0]]

def test_empty_first():
    assert normalize(threeSumFirst([])) == []

def test_empty_second():
    assert normalize(threeSumSecond([])) == []

def test_no_solution_first():
    assert normalize(threeSumFirst([1,2,-2,-1])) == []

def test_no_solution_second():
    assert normalize(threeSumSecond([1,2,-2,-1])) == []

def test_multiple_duplicates_first():
    assert normalize(threeSumFirst([-2,0,0,2,2])) == [[-2,0,2]]

def test_multiple_duplicates_second():
    assert normalize(threeSumSecond([-2,0,0,2,2])) == [[-2,0,2]]

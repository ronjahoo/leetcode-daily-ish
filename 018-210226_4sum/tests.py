from solution import fourSumFirst, fourSumSecond

def test_example1_first():
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    result = sorted([sorted(q) for q in fourSumFirst(nums, target)])
    expected = sorted([[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]])
    assert result == expected

def test_example1_second():
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    result = sorted([sorted(q) for q in fourSumSecond(nums, target)])
    expected = sorted([[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]])
    assert result == expected

def test_empty_input_first():
    assert fourSumFirst([], 0) == []

def test_empty_input_second():
    assert fourSumSecond([], 0) == []

def test_no_quadruplet_first():
    nums = [1, 2, 3, 4]
    target = 100
    assert fourSumFirst(nums, target) == []

def test_no_quadruplet_second():
    nums = [1, 2, 3, 4]
    target = 100
    assert fourSumSecond(nums, target) == []

def test_duplicates_first():
    nums = [2,2,2,2,2]
    target = 8
    result = fourSumFirst(nums, target)
    assert result == [[2,2,2,2]]

def test_duplicates_second():
    nums = [2,2,2,2,2]
    target = 8
    result = fourSumSecond(nums, target)
    assert result == [[2,2,2,2]]

def test_multiple_quadruplets_first():
    nums = [1, 0, -1, 0, -2, 2, 2]
    target = 2
    result = sorted([sorted(q) for q in fourSumFirst(nums, target)])
    expected = sorted([[-2,0,2,2], [-1,0,1,2]])
    assert result == expected

def test_multiple_quadruplets_second():
    nums = [1, 0, -1, 0, -2, 2, 2]
    target = 2
    result = sorted([sorted(q) for q in fourSumSecond(nums, target)])
    expected = sorted([[-2,0,2,2], [-1,0,1,2]])
    assert result == expected
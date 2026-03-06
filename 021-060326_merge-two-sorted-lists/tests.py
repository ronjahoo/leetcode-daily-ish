from solution import (
    mergeTwoListsFirst,
    mergeTwoListsSecond,
)

def make_list(vals):
    from solution import ListNode
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def list_to_arr(node):
    vals = []
    while node:
        vals.append(node.val)
        node = node.next
    return vals

def test_example1_first():
    assert list_to_arr(mergeTwoListsFirst(make_list([1,2,4]), make_list([1,3,4]))) == [1,1,2,3,4,4]

def test_example1_second():
    assert list_to_arr(mergeTwoListsSecond(make_list([1,2,4]), make_list([1,3,4]))) == [1,1,2,3,4,4]

def test_both_empty_first():
    assert list_to_arr(mergeTwoListsFirst(make_list([]), make_list([]))) == []

def test_both_empty_second():
    assert list_to_arr(mergeTwoListsSecond(make_list([]), make_list([]))) == []

def test_one_empty_first():
    assert list_to_arr(mergeTwoListsFirst(make_list([]), make_list([0]))) == [0]

def test_one_empty_second():
    assert list_to_arr(mergeTwoListsSecond(make_list([]), make_list([0]))) == [0]

def test_first_empty_first():
    assert list_to_arr(mergeTwoListsFirst(make_list([]), make_list([1,2,3]))) == [1,2,3]

def test_first_empty_second():
    assert list_to_arr(mergeTwoListsSecond(make_list([]), make_list([1,2,3]))) == [1,2,3]

def test_second_empty_first():
    assert list_to_arr(mergeTwoListsFirst(make_list([1,2,3]), make_list([]))) == [1,2,3]

def test_second_empty_second():
    assert list_to_arr(mergeTwoListsSecond(make_list([1,2,3]), make_list([]))) == [1,2,3]

def test_duplicates_first():
    assert list_to_arr(mergeTwoListsFirst(make_list([1,1,1]), make_list([1,1,1]))) == [1,1,1,1,1,1]

def test_duplicates_second():
    assert list_to_arr(mergeTwoListsSecond(make_list([1,1,1]), make_list([1,1,1]))) == [1,1,1,1,1,1]

def test_negatives_first():
    assert list_to_arr(mergeTwoListsFirst(make_list([-3,-1,2]), make_list([-2,0,3]))) == [-3,-2,-1,0,2,3]

def test_negatives_second():
    assert list_to_arr(mergeTwoListsSecond(make_list([-3,-1,2]), make_list([-2,0,3]))) == [-3,-2,-1,0,2,3]

def test_single_each_first():
    assert list_to_arr(mergeTwoListsFirst(make_list([1]), make_list([2]))) == [1,2]

def test_single_each_second():
    assert list_to_arr(mergeTwoListsSecond(make_list([1]), make_list([2]))) == [1,2]

def test_single_reversed_first():
    assert list_to_arr(mergeTwoListsFirst(make_list([2]), make_list([1]))) == [1,2]

def test_single_reversed_second():
    assert list_to_arr(mergeTwoListsSecond(make_list([2]), make_list([1]))) == [1,2]

def test_interleaved_first():
    assert list_to_arr(mergeTwoListsFirst(make_list([1,3,5]), make_list([2,4,6]))) == [1,2,3,4,5,6]

def test_interleaved_second():
    assert list_to_arr(mergeTwoListsSecond(make_list([1,3,5]), make_list([2,4,6]))) == [1,2,3,4,5,6]

def test_all_same_first():
    assert list_to_arr(mergeTwoListsFirst(make_list([5,5]), make_list([5,5]))) == [5,5,5,5]

def test_all_same_second():
    assert list_to_arr(mergeTwoListsSecond(make_list([5,5]), make_list([5,5]))) == [5,5,5,5]

def test_min_max_values_first():
    assert list_to_arr(mergeTwoListsFirst(make_list([-100]), make_list([100]))) == [-100,100]

def test_min_max_values_second():
    assert list_to_arr(mergeTwoListsSecond(make_list([-100]), make_list([100]))) == [-100,100]
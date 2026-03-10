from solution import (
    mergeKListsFirst,
    mergeKListsSecond,
    make_list,
    ListNode,
)

def to_list(node):
    vals = []
    while node:
        vals.append(node.val)
        node = node.next
    return vals

def test_example1_first():
    lists = [make_list([1, 4, 5]), make_list([1, 3, 4]), make_list([2, 6])]
    assert to_list(mergeKListsFirst(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]

def test_example1_second():
    lists = [make_list([1, 4, 5]), make_list([1, 3, 4]), make_list([2, 6])]
    assert to_list(mergeKListsSecond(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]

def test_empty_lists_first():
    assert to_list(mergeKListsFirst([])) == []

def test_empty_lists_second():
    assert to_list(mergeKListsSecond([])) == []

def test_single_empty_list_first():
    assert to_list(mergeKListsFirst([make_list([])])) == []

def test_single_empty_list_second():
    assert to_list(mergeKListsSecond([make_list([])])) == []

def test_all_empty_lists_first():
    assert to_list(mergeKListsFirst([make_list([]), make_list([]), make_list([])])) == []

def test_all_empty_lists_second():
    assert to_list(mergeKListsSecond([make_list([]), make_list([]), make_list([])])) == []

def test_single_list_first():
    assert to_list(mergeKListsFirst([make_list([1, 2, 3])])) == [1, 2, 3]

def test_single_list_second():
    assert to_list(mergeKListsSecond([make_list([1, 2, 3])])) == [1, 2, 3]

def test_two_lists_first():
    lists = [make_list([1, 2, 4]), make_list([1, 3, 4])]
    assert to_list(mergeKListsFirst(lists)) == [1, 1, 2, 3, 4, 4]

def test_two_lists_second():
    lists = [make_list([1, 2, 4]), make_list([1, 3, 4])]
    assert to_list(mergeKListsSecond(lists)) == [1, 1, 2, 3, 4, 4]

def test_all_same_values_first():
    lists = [make_list([1, 1]), make_list([1, 1]), make_list([1, 1])]
    assert to_list(mergeKListsFirst(lists)) == [1, 1, 1, 1, 1, 1]

def test_all_same_values_second():
    lists = [make_list([1, 1]), make_list([1, 1]), make_list([1, 1])]
    assert to_list(mergeKListsSecond(lists)) == [1, 1, 1, 1, 1, 1]

def test_negative_values_first():
    lists = [make_list([-3, -1, 2]), make_list([-2, 0, 3])]
    assert to_list(mergeKListsFirst(lists)) == [-3, -2, -1, 0, 2, 3]

def test_negative_values_second():
    lists = [make_list([-3, -1, 2]), make_list([-2, 0, 3])]
    assert to_list(mergeKListsSecond(lists)) == [-3, -2, -1, 0, 2, 3]

def test_single_element_lists_first():
    lists = [make_list([3]), make_list([1]), make_list([2])]
    assert to_list(mergeKListsFirst(lists)) == [1, 2, 3]

def test_single_element_lists_second():
    lists = [make_list([3]), make_list([1]), make_list([2])]
    assert to_list(mergeKListsSecond(lists)) == [1, 2, 3]

def test_mixed_empty_and_nonempty_first():
    lists = [make_list([]), make_list([1, 3]), make_list([]), make_list([2, 4])]
    assert to_list(mergeKListsFirst(lists)) == [1, 2, 3, 4]

def test_mixed_empty_and_nonempty_second():
    lists = [make_list([]), make_list([1, 3]), make_list([]), make_list([2, 4])]
    assert to_list(mergeKListsSecond(lists)) == [1, 2, 3, 4]

def test_output_sorted_first():
    lists = [make_list([5, 10, 15]), make_list([1, 8, 12]), make_list([3, 6, 9])]
    result = to_list(mergeKListsFirst(lists))
    assert result == sorted(result)

def test_output_sorted_second():
    lists = [make_list([5, 10, 15]), make_list([1, 8, 12]), make_list([3, 6, 9])]
    result = to_list(mergeKListsSecond(lists))
    assert result == sorted(result)

def test_output_length_first():
    lists = [make_list([1, 2]), make_list([3, 4]), make_list([5])]
    assert len(to_list(mergeKListsFirst(lists))) == 5

def test_output_length_second():
    lists = [make_list([1, 2]), make_list([3, 4]), make_list([5])]
    assert len(to_list(mergeKListsSecond(lists))) == 5

def test_both_agree():
    test_cases = [
        [make_list([1, 4, 5]), make_list([1, 3, 4]), make_list([2, 6])],
        [make_list([]), make_list([1]), make_list([])],
        [make_list([-5, 0, 5]), make_list([-3, 3])],
        [make_list([1, 1, 1]), make_list([1, 1])],
    ]
    for lists_raw in test_cases:
        vals = [to_list(l) for l in lists_raw]
        lists1 = [make_list(v) for v in vals]
        lists2 = [make_list(v) for v in vals]
        assert to_list(mergeKListsFirst(lists1)) == to_list(mergeKListsSecond(lists2))
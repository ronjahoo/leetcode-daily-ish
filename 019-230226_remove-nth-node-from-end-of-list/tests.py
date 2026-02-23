from solution import (
    removeNthFromEndFirst,
    removeNthFromEndSecond,
    build_linked_list,
    linked_list_to_list,
)

def test_example_first():
    head = build_linked_list([1,2,3,4,5])
    result = linked_list_to_list(removeNthFromEndFirst(head, 2))
    assert result == [1,2,3,5]

def test_example_second():
    head = build_linked_list([1,2,3,4,5])
    result = linked_list_to_list(removeNthFromEndSecond(head, 2))
    assert result == [1,2,3,5]

def test_single_element_first():
    head = build_linked_list([1])
    result = linked_list_to_list(removeNthFromEndFirst(head, 1))
    assert result == []

def test_single_element_second():
    head = build_linked_list([1])
    result = linked_list_to_list(removeNthFromEndSecond(head, 1))
    assert result == []

def test_remove_head_first():
    head = build_linked_list([1,2])
    result = linked_list_to_list(removeNthFromEndFirst(head, 2))
    assert result == [2]

def test_remove_head_second():
    head = build_linked_list([1,2])
    result = linked_list_to_list(removeNthFromEndSecond(head, 2))
    assert result == [2]

def test_remove_last_first():
    head = build_linked_list([1,2])
    result = linked_list_to_list(removeNthFromEndFirst(head, 1))
    assert result == [1]

def test_remove_last_second():
    head = build_linked_list([1,2])
    result = linked_list_to_list(removeNthFromEndSecond(head, 1))
    assert result == [1]

def test_empty_input_first():
    result = removeNthFromEndFirst(None, 1)
    assert result is None

def test_empty_input_second():
    result = removeNthFromEndSecond(None, 1)
    assert result is None

def test_longer_list_first():
    head = build_linked_list([1,2,3,4,5,6,7])
    result = linked_list_to_list(removeNthFromEndFirst(head, 4))
    assert result == [1,2,3,5,6,7]

def test_longer_list_second():
    head = build_linked_list([1,2,3,4,5,6,7])
    result = linked_list_to_list(removeNthFromEndSecond(head, 4))
    assert result == [1,2,3,5,6,7]
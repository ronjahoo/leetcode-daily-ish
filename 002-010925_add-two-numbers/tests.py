import pytest
from solution import addTwoNumbersLoop, ListNode

def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out

def test_basic_case():
    number1 = ListNode(2, ListNode(4, ListNode(3)))
    number2 = ListNode(5, ListNode(6, ListNode(4)))
    result = addTwoNumbersLoop(number1, number2)
    assert to_list(result) == [7, 0, 8]

def test_zero_case():
    number1 = ListNode(0)
    number2 = ListNode(0)
    result = addTwoNumbersLoop(number1, number2)
    assert to_list(result) == [0]

def test_large_case():
    number1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    number2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    result = addTwoNumbersLoop(number1, number2)
    assert to_list(result) == [8, 9, 9, 9, 0, 0, 0, 1]
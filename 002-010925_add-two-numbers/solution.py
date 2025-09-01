from typing import List

def addTwoNumbersRec(l1, l2, carry=0):
    if not l1 and not l2 and carry == 0:
        return None
    s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
    carry, digit = divmod(s, 10)
    node = ListNode(digit)
    node.next = addTwoNumbersRec(l1.next if l1 else None,
                                 l2.next if l2 else None,
                                 carry)
    return node

def addTwoNumbersLoop(l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    dummy = ListNode(0)
    tail = dummy
    carry = 0

    p, q = l1, l2
    while p or q or carry:
        x = p.val if p else 0
        y = q.val if q else 0

        s = x + y + carry
        carry, digit = divmod(s, 10)   # digit = s % 10, carry = s // 10

        tail.next = ListNode(digit)
        tail = tail.next

        p = p.next if p else None
        q = q.next if q else None

    return dummy.next

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

if __name__ == "__main__":
    # number1 = [5, 7, 1]
    number1 = ListNode(5, ListNode(7, ListNode(1)))
    # number2 = [1, 5, 1]
    number2 = ListNode(1, ListNode(5, ListNode(1)))

    result = addTwoNumbersLoop(number1, number2)
    result2 = addTwoNumbersRec(number1, number2)

    # Tulostetaan tulos linkitettynä listana
    while result:
        print(result.val, end=" ")
        result = result.next
    while result2:
        print(result2.val, end=" ")
        result2 = result2.next

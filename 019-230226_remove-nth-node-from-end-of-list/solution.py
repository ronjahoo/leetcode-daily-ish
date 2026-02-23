from typing import List, Optional

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEndFirst(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if head is None:
        return None

    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    index_from_start = length - n

    if index_from_start == 0:
        return head.next

    current = head
    for _ in range(index_from_start - 1):
        current = current.next

    current.next = current.next.next

    return head


def removeNthFromEndSecond(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    slow = dummy
    fast = dummy

    for _ in range(n):
        if fast.next is None:
            return head  
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next

def build_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next

def linked_list_to_list(head):
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result

if __name__ == "__main__":
    head1 = build_linked_list([1, 2, 3, 4, 5])
    head2 = build_linked_list([1])
    head3 = build_linked_list([1, 2])

    print("First solution:")
    print(linked_list_to_list(removeNthFromEndFirst(head1, 2)))
    print(linked_list_to_list(removeNthFromEndFirst(head2, 1)))
    print(linked_list_to_list(removeNthFromEndFirst(head3, 1)))

    head1 = build_linked_list([1, 2, 3, 4, 5])
    head2 = build_linked_list([1])
    head3 = build_linked_list([1, 2])

    print("Second solution:")
    print(linked_list_to_list(removeNthFromEndSecond(head1, 2)))
    print(linked_list_to_list(removeNthFromEndSecond(head2, 1)))
    print(linked_list_to_list(removeNthFromEndSecond(head3, 1)))
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def make_list(vals):
    dummy = ListNode()
    cur = dummy

    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next

    return dummy.next

def print_list(node):
    vals = []

    while node:
        vals.append(node.val)
        node = node.next

    print(vals)

def mergeKListsFirst(lists):
    vals = []

    for node in lists:
        while node:
            vals.append(node.val)
            node = node.next

    vals.sort()
    dummy = ListNode()
    cur = dummy

    for val in vals:
        cur.next = ListNode(val)
        cur = cur.next

    return dummy.next

def mergeKListsSecond(lists):
    dummy = ListNode()
    cur = dummy
    heap = []

    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    while heap:
        val, i, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
            
    return dummy.next

if __name__ == "__main__":
    print_list(mergeKListsFirst([make_list([1,4,5]), make_list([1,3,4]), make_list([2,6])]))  # [1,1,2,3,4,4,5,6]
    print_list(mergeKListsFirst([]))                                                           # []
    print_list(mergeKListsFirst([make_list([])]))                                              # []

    print_list(mergeKListsSecond([make_list([1,4,5]), make_list([1,3,4]), make_list([2,6])]))  # [1,1,2,3,4,4,5,6]
    print_list(mergeKListsSecond([]))                                                           # []
    print_list(mergeKListsSecond([make_list([])]))                                              # []
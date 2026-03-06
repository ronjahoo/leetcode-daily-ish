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

def mergeTwoListsFirst(list1, list2):
    vals1, vals2 = [], []
    cur = list1
    while cur:
        vals1.append(cur.val)
        cur = cur.next
    cur = list2
    while cur:
        vals2.append(cur.val)
        cur = cur.next

    result = [0] * (len(vals1) + len(vals2))

    i, j, k = 0, 0, 0
    while i < len(vals1) and j < len(vals2):
        if vals1[i] <= vals2[j]:
            result[k] = vals1[i]
            i += 1
        else:
            result[k] = vals2[j]
            j += 1
        k += 1 
    
    while i < len(vals1):
        result[k] = vals1[i]
        i += 1
        k += 1
    while j < len(vals2):
        result[k] = vals2[j]
        j += 1
        k += 1

    dummy = ListNode()
    cur = dummy
    for val in result:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next


def mergeTwoListsSecond(list1, list2):
    dummy = ListNode()
    cur = dummy

    p1, p2 = list1, list2
    while p1 and p2:
        if p1.val <= p2.val:
            cur.next = p1  
            p1 = p1.next
        else:
            cur.next = p2
            p2 = p2.next
        cur = cur.next

    cur.next = p1 if p1 else p2

    return dummy.next

if __name__ == "__main__":
    list1 = make_list([1, 2, 4])
    list2 = make_list([1,3,4])
    list3 = make_list([])
    list4 = make_list([])
    list5 = make_list([])
    list6 = make_list([0])
    print_list(mergeTwoListsFirst(list1, list2))   
    print_list(mergeTwoListsFirst(list3, list4))   
    print_list(mergeTwoListsFirst(list5, list6))

    list1 = make_list([1, 2, 4])
    list2 = make_list([1,3,4])
    list3 = make_list([])
    list4 = make_list([])
    list5 = make_list([])
    list6 = make_list([0])
    print_list(mergeTwoListsSecond(list1, list2)) 
    print_list(mergeTwoListsSecond(list3, list4))  
    print_list(mergeTwoListsSecond(list5, list6))
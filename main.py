# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# def mergeTwoLists(self, list1, list2):
def mergeTwoLists(list1, list2):

    # if either list is empty, return the other list
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    # both lists have nodes in them, so combine them
    a = list1
    b = list2
    c = None  # initialize third list pointer to an empty list
    # c is a pointer that moves down the list. list3 will point to the head later

    while a is not None and b is not None:
        # there are more nodes in both lists
        if a.val <= b.val:
            newNode = ListNode(a.val)
            if c is None:
                c = newNode
                list3 = c       # list3 is a header pointer to the new third list
            else:
                c.next = newNode
                c = c.next
            a = a.next
        else:
            newNode = ListNode(b.val)
            if c is None:
                c = newNode
                list3 = c       # list3 is a header pointer to the new third list
            else:
                c.next = newNode
                c = c.next
            b = b.next

    if a is None:
        c.next = b
    else:
        c.next = a

    return list3


if __name__ == '__main__':
    # list3 = mergeTwoLists(list1, list2)
    print("hello")


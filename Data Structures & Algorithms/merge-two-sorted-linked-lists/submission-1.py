# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        l = dummy

        one = list1
        two = list2

        while one is not None and two is not None:

            if one.val < two.val:
                l.next = one
                one = one.next
            else:
                l.next = two
                two = two.next

            l = l.next

        if one is not None:
            l.next = one
        else:
            l.next = two

        return dummy.next
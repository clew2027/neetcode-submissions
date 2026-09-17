# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        right = dummy
        left = dummy
        count = 0

        while count < n :
            right = right.next
            count+=1


        while right != None and right.next !=None:
            right = right.next
            left = left.next
        print(left.val)

        if left.next:
            left.next = left.next.next
        else:
            return None
        return dummy.next

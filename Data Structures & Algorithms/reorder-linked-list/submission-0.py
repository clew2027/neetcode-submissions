# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return head
        
        n = self.reverse(head.next)
        head.next.next = head
        head.next = None

        return n




    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = head

        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        #merge
        second = slow.next
        slow.next = None
        first = head
        second = self.reverse(second)

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

    

        


        
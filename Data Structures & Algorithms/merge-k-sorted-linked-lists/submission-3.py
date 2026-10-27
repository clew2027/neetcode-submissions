# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        result = ListNode(0)
        curr = result
        counter = 0
        for l in lists:
            if l is not None:
                heapq.heappush(heap, (l.val, counter, l))
                counter+= 1
        heapq.heapify(heap)
        
        while heap:
            val, c, popped = heapq.heappop(heap)
            curr.next = popped
            if popped.next is not None:
                heapq.heappush(heap, (popped.next.val, counter, popped.next))
                counter += 1
            curr = curr.next
        return result.next




        
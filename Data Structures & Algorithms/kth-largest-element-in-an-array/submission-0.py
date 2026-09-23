class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []

        for num in nums:
            heapq.heappush(max_heap, -num)
        kmax = 0
        for i in range(k):
            kmax = -heapq.heappop(max_heap)

        return kmax


        
        
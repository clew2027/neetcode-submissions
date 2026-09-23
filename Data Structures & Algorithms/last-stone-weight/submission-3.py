import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for num in stones: 
            heapq.heappush(max_heap, -num)
        
        while len(max_heap) > 1:
            max1 = -heapq.heappop(max_heap)
            max2 = -heapq.heappop(max_heap)
            print(max1)
            print(max2)

            if abs(max1 - max2) != 0:
                heapq.heappush(max_heap, -abs(max1 - max2))

        if len(max_heap) == 0:
            return 0
        else: 
            return -heapq.heappop(max_heap)

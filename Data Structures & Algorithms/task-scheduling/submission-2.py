import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        maxheap = []
        for f in freq.values():
            heapq.heappush(maxheap, -f)

        count = 0
        waiting = []
        while maxheap or len(waiting) > 0:
            if len(waiting) > 0 and waiting[0][1] == count:
                heapq.heappush(maxheap, waiting[0][0])
                waiting.remove(waiting[0])
            if maxheap:
                frequency =  heapq.heappop(maxheap)
                if frequency < -1:
                    frequency +=1 
                    waiting.append((frequency, count + n + 1))
            count += 1
        return count



        
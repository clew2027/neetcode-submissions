import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        heap = [-v for v in freq.values()]
        heapq.heapify(heap)
        
        cooldown = deque() #remaining freq, when can start again
        count = 0
        while heap or cooldown:
            if cooldown and cooldown[0][1] == count:
                f, time = cooldown.popleft()
                if f < 0:
                    heapq.heappush(heap, f)
            if heap:
                f = heapq.heappop(heap)
                if f + 1 < 0:
                    cooldown.append((f + 1, count + n + 1))
            count += 1
        return count



            





        
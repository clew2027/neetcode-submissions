class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indeg = [0] * numCourses
        for l in prerequisites:
            course = l[0]
            prereq = l[1] 
            adj[prereq].append(course)
            indeg[course] += 1
        q = deque()
        for i in range(len(indeg)):
            if indeg[i] == 0:
                q.append(i)
        finished = 0
        while q:
            finished += 1
            c = q.popleft()
            pre_c = adj[c]
            print(pre_c)
            for p in pre_c:
                indeg[p] -= 1
                if indeg[p] == 0:
                    q.append(p)
        return finished == numCourses
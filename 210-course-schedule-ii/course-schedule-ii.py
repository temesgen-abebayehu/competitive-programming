class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = defaultdict(int)
        graph = defaultdict(set)
        for i, j in prerequisites:
            graph[j].add(i)
            pre[i] += 1

        res = []
        que = deque()
        for i in range(numCourses):
            if pre[i] == 0:
                que.append(i)
                   
        while que:
            node = que.popleft()
            for i in graph[node]:
                pre[i] -= 1
                if pre[i] == 0:
                    que.append(i)
            res.append(node)

        if len(res) != numCourses:
            return []
            
        return res
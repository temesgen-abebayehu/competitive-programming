class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)
        closure = defaultdict(set)

        for u, v in prerequisites:
            graph[u].add(v)

        for node in range(numCourses):
            visited = set()
            que = deque([node])

            while que:
                curr = que.popleft()
                if curr in visited:
                    continue

                visited.add(curr)
                for negn in graph[curr]:
                    que.append(negn)
                    closure[node].add(negn)

        res = []
        for u, v in queries:
            res.append(v in closure[u])

        return res

        
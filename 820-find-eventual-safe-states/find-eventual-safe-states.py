class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        rev_graph = defaultdict(set)
        outward = defaultdict(int)
        que = deque()

        for u in range(n):
            for v in graph[u]:
                rev_graph[v].add(u)
                outward[u] += 1
            # if the node is terminal(safe state)
            if len(graph[u]) == 0:
                que.append(u)

        safe = []
        while que:
            node = que.popleft()
            safe.append(node)

            for u in rev_graph[node]:
                outward[u] -= 1
                if outward[u] == 0:
                    que.append(u)

        return sorted(safe)
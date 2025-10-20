class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, path):
            if node == n-1:
                ans.append(path[:])
                return

            for neighbor in direct[node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()

            return 

        n = len(graph)
        direct = defaultdict(list)
        ans = []

        for i in range(n):
            for node in graph[i]:
                direct[i].append(node)
        
        dfs(0, [0])

        return ans

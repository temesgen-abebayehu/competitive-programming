class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a,b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1/v

        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1
            if start == end:
                return 1

            visited.add(start)

            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return result * weight
            return -1

        ans = []
        for a,b in queries:
            ans.append(dfs(a,b,set()))

        return ans
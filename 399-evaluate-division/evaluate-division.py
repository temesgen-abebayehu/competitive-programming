class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        # Build the graph
        for (A, B), value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1.0 / value

        print(graph)
        
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return weight * result
            return -1.0
        
        results = []
        for C, D in queries:
            visited = set()
            results.append(dfs(C, D, visited))
        return results
        
                
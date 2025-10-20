class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node, visited):
            if node == destination:
                return True

            visited.add(node)

            for v in graph[node]:
                if v not in visited:
                    found = dfs(v, visited)
                    if found:
                        return True
                    

            return False


        graph = defaultdict(set)
        visited = set()
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)

        
        return dfs(source, visited)
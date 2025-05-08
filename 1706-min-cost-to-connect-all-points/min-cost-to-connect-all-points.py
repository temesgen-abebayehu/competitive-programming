class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        
        def union(w, x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    root[rootY] = rootX
                    size[rootX] += size[rootY]
                else:
                    root[rootX] = rootY
                    size[rootY] += size[rootX]
                
                self.weight += w


        n = len(points)
        root = [i for i in range(n)]
        size = [1] * n
        self.weight = 0

        graph = []
        for i in range(n):
            for j in range(i+1, n):
                w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph.append((w, i, j))

        graph.sort()
        for edge in graph:
            w, x, y = edge
            union(w, x, y)
        return self.weight
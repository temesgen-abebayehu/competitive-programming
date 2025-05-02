class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {i:i for i in range(1, len(edges) + 1)}
        size = [1] * (len(edges) + 1)
        ans = [0] * 2

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                if size[root_x] > size[root_y]:
                    parent[root_y] = root_x
                    size[root_x] += size[root_y]

                else:
                    parent[root_x] = root_y
                    size[root_y] += size[root_x]

            else:
                ans[0] = x
                ans[1] = y

        for x, y in edges:
            union(x, y)

        return ans

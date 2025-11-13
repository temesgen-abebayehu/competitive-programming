class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for _ in range(size)]
        self.count = size

    def find(self, i):
        if self.root[i] == i:
            return i
        self.root[i] = self.find(self.root[i])  # Path compression
        return self.root[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] > self.rank[root_j]:
                self.root[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.root[root_i] = root_j
            else:
                self.root[root_j] = root_i
                self.rank[root_i] += 1
            self.count -= 1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
                    
        return uf.count
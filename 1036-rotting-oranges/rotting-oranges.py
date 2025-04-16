class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def inbound(i, j):
            return 0<=i<n and 0<=j<m
        dir = [[0,-1], [-1, 0], [1, 0], [0, 1]]

        que = deque()
        fresh = time = 0
        visted = set()

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    que.append([r,c])

                elif grid[r][c] == 1:
                    fresh += 1

        while que and fresh !=0:
            l = len(que)
            for i in range(l):
                r, c = que.popleft()
                for dr, dc in dir:
                    if inbound(dr + r, dc + c) and grid[dr+r][dc+c] == 1:
                        grid[dr+r][dc+c] = 2
                        fresh -= 1
                        que.append([dr+r, dc+c])
            time += 1
        return time if fresh == 0 else -1
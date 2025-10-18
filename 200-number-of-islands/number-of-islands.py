import numpy as np
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        # for checking the index is bounded
        def is_bound(r,c):
            return 0 <= r < row and 0 <= c < col
        
        neighbor = [[1,0], [0,1], [-1,0], [0,-1]]

        def bfs(i,j):
            queue = deque([(i,j)])

            # mark as visited
            grid[i][j] = "0"

            while queue:
                ci, cj = queue.popleft()
                for ni, nj in neighbor:
                    if is_bound(ci+ni, cj+nj) and grid[ci+ni][cj+nj] == "1":
                        queue.append((ci+ni, cj+nj))
                        # mark as visited
                        grid[ci+ni][cj+nj] = "0"


        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i,j)

        return count




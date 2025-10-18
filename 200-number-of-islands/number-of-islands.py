import numpy as np
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        # for checking the index is bounded
        def is_bound(r,c):
            return 0 <= r < row and 0 <= c < col

        def dfs(i,j):
            if is_bound(i,j) and grid[i][j] == "1":
                grid[i][j] = "0"

                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)

        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i,j)

        return count




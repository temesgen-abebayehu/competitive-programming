class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}

        def dp(i, j):
            if i == len(grid)-1 and j == len(grid[0])-1:
                return grid[i][j]

            if i == len(grid) or j == len(grid[0]):
                return float('inf')

            if (i,j) in memo:
                return memo[(i,j)]

            res = grid[i][j] + min(dp(i+1, j), dp(i, j+1))

            memo[(i,j)] = res
            return res

        return dp(0,0)
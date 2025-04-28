class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        row = len(grid)
        col = len(grid[0])
        for r in range(row-1, -1, -1):
            for c in range(col-1, -1, -1):
                if grid[r][c] < 0:
                    ans += 1
                else:
                    break
        return ans
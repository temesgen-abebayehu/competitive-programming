class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        def inbound(row, col):
            return 0<=row<rows and 0<=col<cols

        dir = [(0,1), (0,-1), (1, 0), (-1, 0)]

        def dfs(row, col):
            if not inbound(row, col) or grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            curr_area = 1

            for x, y in dir:
                new_row = row + x
                new_col = col + y

                curr_area += dfs(new_row, new_col)

            return curr_area



        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(max_area, area)

        return max_area

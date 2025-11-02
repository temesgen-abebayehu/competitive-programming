class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        dirc = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        queue = deque()
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append([row, col])
                elif grid[row][col] == 1:
                    fresh += 1

        # Fixed variable name - use 'fresh' instead of 'fresh_count'
        if fresh == 0:
            return 0

        time = 0

        while queue:
            size = len(queue)
            # Only increment time if we actually rotted any oranges in this minute
            rotted_this_minute = False
            
            for i in range(size):
                row, col = queue.popleft()
                for r, c in dirc:
                    new_row = row + r
                    new_col = col + c

                    if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        queue.append([new_row, new_col])
                        fresh -= 1
                        rotted_this_minute = True
            
            # Only increment time if we rotted oranges in this iteration
            if rotted_this_minute:
                time += 1

        return time if fresh == 0 else -1
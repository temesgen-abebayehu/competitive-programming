from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        def inbound(i, j):
            return 0 <= i < len(mat) and 0 <= j < len(mat[0])
        
        direction = 1  # 1 for upward, -1 for downward
        ans = []
        rows = len(mat)
        cols = len(mat[0])
        row, col = 0, 0

        for _ in range(rows * cols):
            ans.append(mat[row][col])

            # Calculate the next cell in the current direction
            new_row = row + (-1 if direction == 1 else 1)
            new_col = col + (1 if direction == 1 else -1)

            if inbound(new_row, new_col):
                row, col = new_row, new_col
            else:
                if direction == 1:
                    # If we are moving upwards and hit the boundary
                    if col == cols - 1:
                        row += 1
                    else:
                        col += 1
                else:
                    # If we are moving downwards and hit the boundary
                    if row == rows - 1:
                        col += 1
                    else:
                        row += 1
                direction *= -1  # Change direction

        return ans
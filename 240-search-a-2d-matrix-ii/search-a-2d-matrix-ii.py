class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols


        row = 0
        col = cols - 1

        while inbound(row, col):
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                row += 1
            else:
                col -= 1

        return False
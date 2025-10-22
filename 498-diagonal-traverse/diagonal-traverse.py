class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        dirc = True  # True = upward and False = downward
        result = []
        row = 0
        col = 0

        for k in range(rows*cols):
            result.append(mat[row][col])

            if dirc:
                if col == cols - 1:
                    row += 1
                    dirc = False
                elif row == 0:
                    col += 1
                    dirc = False
                else:
                    row -= 1
                    col += 1
            else:
                if row == rows - 1:
                    col += 1
                    dirc = True
                elif col == 0:
                    row += 1
                    dirc = True
                else:
                    row += 1
                    col -= 1

        return result
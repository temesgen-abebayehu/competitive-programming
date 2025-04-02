class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            l = 0
            r = len(matrix[i]) - 1
            while l <= r:
                m = (l+r)//2
                if target == matrix[i][m]:
                    return True
                elif target > matrix[i][m]:
                    l = m + 1
                else:
                    r = m - 1
        else:
            return False
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        def isBound(i, j):
            return 0 <= i < len(self.matrix) and 0 <= j < len(self.matrix[0])

        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                self.matrix[row][col] = self.matrix[row][col]
                if isBound(row-1, col):
                    self.matrix[row][col] += self.matrix[row-1][col]
                if isBound(row, col-1):
                    self.matrix[row][col] += self.matrix[row][col-1]
                if isBound(row-1, col-1):
                    self.matrix[row][col] -= self.matrix[row-1][col-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        def isBound(i, j):
            return 0 <= i < len(self.matrix) and 0 <= j < len(self.matrix[0])

        ans = self.matrix[row2][col2]
        if isBound(row1 - 1, col2):
            ans -= self.matrix[row1 - 1][col2]
        if isBound(row2, col1 - 1):
            ans -= self.matrix[row2][col1 - 1]
        if isBound(row1 - 1, col1 - 1):
            ans += self.matrix[row1 - 1][col1 - 1]
        
        return ans



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
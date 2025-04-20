class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row, cols, diags, anti_diags, path):
            if row == n:
                res.append([''.join(row) for row in path])
                return
            for col in range(n):
                diag = row - col
                anti_diag = row + col
                if col in cols or diag in diags or anti_diag in anti_diags:
                    continue
                cols.add(col)
                diags.add(diag)
                anti_diags.add(anti_diag)
                path[row][col] = 'Q'
                backtrack(row + 1, cols, diags, anti_diags, path)
                path[row][col] = '.'
                cols.remove(col)
                diags.remove(diag)
                anti_diags.remove(anti_diag)
        
        res = []
        empty_board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return res
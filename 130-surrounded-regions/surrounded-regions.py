class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        def dfs(i,j):
            if i>=rows or i<0 or j>=cols or j<0 or board[i][j] == 'X' or board[i][j] == 'S':
                return 

            board[i][j] = 'S'
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

      
        for i in range(cols):
            dfs(0,i) # top
            dfs(rows-1,i) # bottom
        
                
        
        for i in range(rows):
            dfs(i,0) # left
            dfs(i, cols-1) # right
                

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'S':
                    board[i][j] = 'O'
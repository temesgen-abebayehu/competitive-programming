class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        dir = [(1,0), (-1,0), (0,-1), (0,1)]

        ans = [[-1] * cols for _ in range(rows)]
        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row, col))
                    ans[row][col] = 0

        
        while queue:
            row, col = queue.popleft()
            for r, c in dir:
                nr = row + r
                nc = col + c
                if inbound(nr, nc) and ans[nr][nc] == -1:
                    ans[nr][nc] = ans[row][col] + 1
                    queue.append((nr, nc))
        return ans
                    

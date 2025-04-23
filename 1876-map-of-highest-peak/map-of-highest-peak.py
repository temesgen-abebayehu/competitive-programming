class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])
        def is_bound(i,j):
            return 0<=i<n and 0<=j<m

        que = deque()
        height = []
        for i in range(n):
            height.append([-1]*m)
        
        for r in range(n):
            for c in range(m):
                if isWater[r][c] == 1:
                    que.append([r,c])
                    height[r][c] = 0
                
        dir = [[0,1], [1,0], [-1,0], [0,-1]]

        while que:
            r,c = que.popleft()
            for dr, dc in dir:
                cr = r + dr
                cc = c + dc
                if is_bound(cr, cc) and height[cr][cc] == -1:
                    height[cr][cc] = height[r][c] + 1
                    que.append([cr,cc])

        return height
        
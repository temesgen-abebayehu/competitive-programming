class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        if not obstacleGrid or not obstacleGrid[0]:
            return 0

        if obstacleGrid[0][0] or obstacleGrid[n-1][m-1]:
            return 0

        # memmorization
        memo = {}

        def dp(i,j):
            if i >= n or j >= m or obstacleGrid[i][j] == 1:
                return 0

            if i == n-1 and j == m-1:
                return 1

            if (i,j) in memo:
                return memo[(i,j)]

            right = dp(i, j+1)
            bottom = dp(i+1, j)

            memo[(i,j)] = right + bottom

            return memo[(i,j)]

        return dp(0,0)
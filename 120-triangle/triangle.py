class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        # bottom-up dp
        dp = [[inf] * n for _ in range(n)]
        for i in range(n):
            dp[n-1][i] = triangle[n-1][i]
        
        for i in range(n-2, -1,-1):
            for j in range(i+1):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])

        
        return dp[0][0]
        
        
        # top-down dp
        # memo = {}

        # def dp(i, j):
        #     if i == n-1:
        #         return triangle[i][j]

        #     state = (i,j)
        #     if state in memo:
        #         return memo[state]

        #     res = triangle[i][j] + min(dp(i+1, j), dp(i+1, j+1))
        #     memo[state] = res
        #     return res

        # return dp(0,0)
            
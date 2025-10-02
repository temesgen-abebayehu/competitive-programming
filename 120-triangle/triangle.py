class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        memo = {}

        def dp(i, j):
            if i == n-1:
                return triangle[i][j]

            state = (i,j)
            if state in memo:
                return memo[state]

            res = triangle[i][j] + min(dp(i+1, j), dp(i+1, j+1))
            memo[state] = res
            return res

        return dp(0,0)
            
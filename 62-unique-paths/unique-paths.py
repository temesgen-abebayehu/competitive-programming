class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dp(i, j):
            if i == m-1 and j == n-1:
                return 1

            if i == m or j == n:
                return 0

            if (i, j) in memo:
                return memo[(i , j)]

            res = dp(i, j+1) + dp(i+1, j)

            memo[(i, j)] = res
            return res

        return dp(0 , 0)
            
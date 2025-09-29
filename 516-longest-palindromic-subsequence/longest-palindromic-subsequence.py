class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for i in range(n-1, -1, -1):
            for r in range(i+1, n):
                if s[i] == s[r]:
                    dp[i][r] = dp[i+1][r-1] + 2
                else:
                    dp[i][r] = max(dp[i+1] [r], dp[i][r-1])

        return dp[0][n-1]
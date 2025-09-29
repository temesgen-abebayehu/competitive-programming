class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}

        def dp(l, r):
            if l == r:
                return 1
            if l > r:
                return 0
            
            state = (l, r)
            if state in memo:
                return memo[state]

            if s[l] == s[r]:
                memo[state] = dp(l+1, r-1) + 2
            else:
                memo[state] = max(dp(l+1, r), dp(l, r-1))

            return memo[state]

        return dp(0, len(s)-1)
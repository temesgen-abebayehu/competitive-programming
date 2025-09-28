class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        memo = {}
        end = n

        def dp(start):
            if start == n:
                return True

            if start in memo:
                return memo[start]

            for end in range(start, n):
                curr_word = s[start:end + 1]

                if curr_word in words:
                    if dp(end + 1):
                        memo[start] = True
                        return memo[start]

            memo[start] = False
            return memo[start]

        return dp(0)

            

            
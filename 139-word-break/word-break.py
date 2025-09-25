class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                curr_word = s[i : j + 1]
                
                if curr_word in word_set and dp[j + 1]:
                    dp[i] = True
                    break 
        
        return dp[0]
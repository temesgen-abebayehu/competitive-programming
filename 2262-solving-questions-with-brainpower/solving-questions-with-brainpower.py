class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:        
        n = len(questions)
        # top-dowm dp

        memo = {}

        def dp(i):
            if i >= n:
                return 0

            if i in memo:
                return memo[i]

            res = max(dp(i+1), questions[i][0] + dp(i + questions[i][1] + 1))
            
            memo[i] = res
            return res

        return dp(0)
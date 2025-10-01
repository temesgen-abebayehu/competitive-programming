class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:        
        n = len(questions)
        # bottom-up dp
        dp = [0] * n
        dp[n-1] = questions[n-1][0]


        for i in range(n-2,-1,-1):            
            if i + questions[i][1] + 1 < n:
                dp[i] = max(dp[i+1], questions[i][0] + dp[i + questions[i][1] + 1])
            else:
                dp[i] = max(questions[i][0], dp[i+1])


        return dp[0]



        # top-dowm dp

        # memo = {}

        # def dp(i):
        #     if i >= n:
        #         return 0

        #     if i in memo:
        #         return memo[i]

        #     res = max(dp(i+1), questions[i][0] + dp(i + questions[i][1] + 1))
            
        #     memo[i] = res
        #     return res

        # return dp(0)
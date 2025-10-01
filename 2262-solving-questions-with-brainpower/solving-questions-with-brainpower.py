class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = {}

        def dp(i):
            if i >= n:
                return 0

            if i in memo:
                return memo[i]

            # not take
            res = dp(i+1)
            print(res,'---')
            # take
            res = max(res, questions[i][0] + dp(i + questions[i][1] + 1))
            
            memo[i] = res
            print(res, i)
            return res

        return dp(0)
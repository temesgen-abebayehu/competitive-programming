class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dp(i):
            if i == 0:
                return cost[i]
            if i == 1:
                return cost[i]
            
            if i in memo:
                return memo[i]

            res =  cost[i] + min(dp(i-1), dp(i-2))

            memo[i] = res
            return res

        return min(dp(len(cost) - 1), dp(len(cost) - 2))
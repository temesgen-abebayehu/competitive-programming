class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def dp(i, a):
            if i < 0 and a > 0:
                return float('inf')

            if i < 0:
                return 0

            if (i,a) in memo:
                return memo[(i,a)]

            res = dp(i-1, a)
            if a >= coins[i]:
                res = min(res, 1 + dp(i, a - coins[i]))
            

            memo[(i,a)] = res
            return res

        coin = dp(len(coins)-1, amount) 
        return -1 if coin == float('inf') else coin

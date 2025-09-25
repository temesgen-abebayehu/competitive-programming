class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}

        def dp(i, hold):
            if i < 0:
                if hold:
                    return float('-inf')
                else:
                    return 0

            if (i, hold) in memo:
                return memo[(i, hold)]

            # not take
            res = dp(i-1, hold)

            # take
            if hold:
                res = max(res, dp(i-1, not hold)- prices[i])

            else:
                res = max(res, dp(i-1, not hold) + prices[i] - fee)

            memo[(i, hold)] = res
            return res

        return dp(len(prices)-1, False)


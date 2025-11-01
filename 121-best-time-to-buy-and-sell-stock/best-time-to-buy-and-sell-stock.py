class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        buy = prices[0]
        for price in prices:
            if price < buy:
                buy = price
            else:
                max_price = max(max_price, price - buy)

        return max_price
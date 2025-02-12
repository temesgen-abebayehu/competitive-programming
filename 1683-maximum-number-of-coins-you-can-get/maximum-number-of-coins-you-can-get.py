class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        l = 1
        r = len(piles)
        result = 0

        while l < r:
            result += piles[l]
            l += 2
            r -= 1

        return result
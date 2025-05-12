class Solution:
    def maxProduct(self, n: int) -> int:
        n = list(str(n))
        n.sort(reverse=True)
        return int(n[0]) * int(n[1])
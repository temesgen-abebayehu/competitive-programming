class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
            if n <= 1:
                return 1
            return n * factorial(n-1)
            
        lead = factorial(n)
        ans = 0
        while lead > 9:
            if lead % 10 == 0:
                ans += 1
            else:
                break
            lead //=10

        return ans
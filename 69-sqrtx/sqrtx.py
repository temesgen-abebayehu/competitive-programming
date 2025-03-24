class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        h = x

        while l <= h:
            m = (l + h) // 2
            if m**2 <= x:
                l = m + 1                
            else:
                h = m - 1
        return h
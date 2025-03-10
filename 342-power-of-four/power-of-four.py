class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def power(f):
            if f >= n:
                return f
            
            return power(4*f)

        ans = power(1)
        if ans == n:
            return True
        else:
            return False
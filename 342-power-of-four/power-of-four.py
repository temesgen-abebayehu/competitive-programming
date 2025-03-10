class Solution:
    def isPowerOfFour(self, n, f=1) -> bool:
        if f == n:
            return True
        elif f> n:
            return False
        
        return self.isPowerOfFour(n, 4*f)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        s = list(str(x))
        return s == list(reversed(s))
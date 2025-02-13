class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        flag = True
        while l<r:
            if s[l] == s[r]:
                l +=1
                r-=1
            elif s[l:r] == s[l:r][::-1] and flag:
                r -= 1
                flag = False
            elif s[l+1:r+1] == s[l+1:r+1][::-1] and flag:
                l +=1
                flag = False            
            else:
                return False
            
        return True
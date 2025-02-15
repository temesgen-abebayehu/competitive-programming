class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        s = [c for c in s]
        l = 0
        r = n-1
        ans = 0
        while l < r:
            if s[l] == '0':
                l+=1
            elif s[r] == '1':
                r-=1
            else:
                s[l], s[r] = s[r], s[l]
                ans += (r-l)
                l+=1
                r-=1

        return ans
                
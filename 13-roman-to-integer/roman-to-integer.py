class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        pre = s[0]
        num = roman[s[0]]

        for i in range(1, len(s)):
            num += roman[s[i]]
            if roman[s[i]] > roman[pre]:
                num -= (2*roman[pre])
            pre = s[i]

        return num
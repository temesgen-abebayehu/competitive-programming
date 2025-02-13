class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        l = 0
        r = 1
        cur_wind = set()
        cur_wind.add(s[0])
        max_len = 1
        while r<len(s):            
            if s[r] in cur_wind:
                cur_wind.remove(s[l])
                l += 1                
            else:
                cur_wind.add(s[r])
                r += 1                
            max_len = max(max_len, r-l)

        return max_len
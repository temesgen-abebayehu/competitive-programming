class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
            
        l = 0
        r = 1
        max_len = 1
        while r<len(s):
            if s[r] in s[l:r]:
                l += 1
            else:
                r += 1
            max_len = max(max_len, r-l)

        return max_len
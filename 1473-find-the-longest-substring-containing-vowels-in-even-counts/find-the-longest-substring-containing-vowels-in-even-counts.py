class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel = {'a':2, 'e':4, 'i':8, 'o':16, 'u':32}
        n = len(s)
        pref = [0] * (n+1)

        for i in range(n):
            if s[i] in vowel:
                pref[i+1] = pref[i] ^ vowel[s[i]]
            else:
                pref[i+1] = pref[i]

        bit = {}
        res = 0
        for i in range(n+1):
            if pref[i] in bit:
                res = max(res, i - bit[pref[i]])
            else:
                bit[pref[i]] = i

        return res
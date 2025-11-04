class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        isomorphic_s = {}
        isomorphic_t = {}
        for i in range(len(s)):
            if s[i] not in isomorphic_s:
                isomorphic_s[s[i]] = t[i]

            elif isomorphic_s[s[i]] != t[i]:
                    return False

            if t[i] not in isomorphic_t:
                isomorphic_t[t[i]] = s[i]
            elif isomorphic_t[t[i]] != s[i]:
                return False
                
        return True
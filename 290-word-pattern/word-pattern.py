class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        follow_p = {}
        follow_s = {}

        s = s.split(' ')

        if len(s) != len(pattern):
            return False
        
        for i in range(len(s)):
            if pattern[i] not in follow_p:
                follow_p[pattern[i]] = s[i]
            elif follow_p[pattern[i]] != s[i]:
                return False
            
            if s[i] not in follow_s:
                follow_s[s[i]] = pattern[i]
            elif follow_s[s[i]] != pattern[i]:
                return False

        return True
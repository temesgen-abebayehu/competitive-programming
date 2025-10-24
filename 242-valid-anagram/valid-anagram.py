class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = Counter(s)
        count_t = Counter(t)

        for k,v in count_s.items():
            if count_t[k] != v:
                return False

        return True
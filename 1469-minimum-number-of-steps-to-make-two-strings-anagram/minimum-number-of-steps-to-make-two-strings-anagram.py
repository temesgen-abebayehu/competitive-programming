class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)

        ans = 0
        for k, v in count_s.items():
            if k not in count_t:
                ans += v
            elif v - count_t[k] > 0:
                ans += v - count_t[k]

        return ans
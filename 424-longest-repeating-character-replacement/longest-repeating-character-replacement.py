class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = defaultdict(int)
        max_freq = 0
        ans = 0
        l = 0

        for r  in range(len(s)):
            dic[s[r]] += 1
            max_freq = max(max_freq, dic[s[r]])

            if (r-l+1) - max_freq > k:
                dic[s[l]] -= 1
                l += 1

            ans = max(ans, r-l+1)

        return ans
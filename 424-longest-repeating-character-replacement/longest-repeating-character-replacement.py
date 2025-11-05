class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        max_freq = 0
        ans = 0
        l = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])

            if r - max_freq - l >= k:
                freq[s[l]] -= 1
                l+=1
            ans = max(ans, r-l+1)
        
        return ans
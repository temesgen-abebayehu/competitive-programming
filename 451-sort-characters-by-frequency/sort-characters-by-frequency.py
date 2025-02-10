class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        ans = []
        for key, value in freq:
            ans.append(key * value)

        return ''.join(ans)
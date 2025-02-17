class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)
        freq_occur = Counter(freq.values())
        if len(freq_occur) == 1 and (1 in freq_occur or 1 in freq_occur.values()):
            return True

        if len(freq_occur) == 2:
            if 1 in freq_occur.keys() and freq_occur[1] == 1:
                return True
            key = sorted(freq_occur.keys())
            if key[1] - key[0] == 1 and freq_occur[key[1]] == 1:
                return True
        
        return False

class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)
        result = Counter(freq.values())
        
        if len(freq) == 1 or (len(result) == 1 and 1 in result.keys()):
            return True

        
        if len(result) == 2:
            key = sorted(list(result.keys()))
            if key[1] - key[0] == 1 and result[key[1]] == 1:
                return True
            if 1 in result.values() and result[1] == 1:
                return True

        return False
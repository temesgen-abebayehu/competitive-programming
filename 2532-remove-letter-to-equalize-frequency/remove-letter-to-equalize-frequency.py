class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)
        
        for char in word:
            # Try removing this character
            freq[char] -= 1
            if freq[char] == 0:
                del freq[char]
            
            # Check if all remaining frequencies are equal
            if len(set(freq.values())) == 1:
                return True
            
            # Restore the frequency
            freq[char] += 1
        
        return False
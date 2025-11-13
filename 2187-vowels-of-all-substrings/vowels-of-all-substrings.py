class Solution:
    def countVowels(self, word: str) -> int:
        total_vowels = 0
        n = len(word)
        vowels = "aeiou"

        for i, char in enumerate(word):
            if char in vowels:
                contribution = (i + 1) * (n - i)
                total_vowels += contribution
        
        return total_vowels
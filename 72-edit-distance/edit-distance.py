class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        memo = {}
        
        def dp(i, j):
            # Base cases
            if i < 0:  # word1 is exhausted, insert all remaining characters of word2
                return j + 1
            if j < 0:  # word2 is exhausted, delete all remaining characters of word1
                return i + 1

            if (i,j) in memo:
                return memo[(i,j)]
            
            # If characters match, no operation needed
            if word1[i] == word2[j]:
                memo[(i,j)] = dp(i-1, j-1)
            
            # Characters don't match - consider all three operations
            else:
                memo[(i,j)] = 1 + min(
                    dp(i-1, j-1),  # Replace
                    dp(i-1, j),    # Delete from word1
                    dp(i, j-1)     # Insert into word1
                )

            return memo[(i,j)]
        
        return dp(n-1, m-1)
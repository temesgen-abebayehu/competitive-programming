class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)  # Convert to set for O(1) lookups
        memo = {}  # Memoization cache
        
        def dfs(start):
            """
            Returns all possible sentences that can be formed from s[start:]
            """
            # Base case: if we've reached the end of string
            if start == len(s):
                return [""]  # Return list with empty string
            
            # If we've already computed result for this start position
            if start in memo:
                return memo[start]
            
            sentences = []  # Store all valid sentences from this position
            
            # Try all possible end positions
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]  # Current candidate word
                
                # If this word is in dictionary
                if word in word_set:
                    # Get all possible sentences from the remaining string
                    next_sentences = dfs(end)
                    
                    # Combine current word with each next sentence
                    for sentence in next_sentences:
                        if sentence:  # If there's more text after
                            sentences.append(word + " " + sentence)
                        else:  # If this is the last word
                            sentences.append(word)
            
            # Store in memo before returning
            memo[start] = sentences
            return sentences
        
        return dfs(0)
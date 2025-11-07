class Solution:
    def longestBalanced(self, s: str) -> int:
        max_balance = 0
        for i in range(len(s)):
            # track frequncy of each word start from index 'i'
            freq = defaultdict(int)
            # iterate over all sub string to get max balanced
            for j in range(i, len(s)):
                freq[s[j]] += 1
                
                # if balanced update the max balanced sub string 
                if len(set(freq.values())) == 1:
                    max_balance = max(max_balance, j-i+1)

        return max_balance

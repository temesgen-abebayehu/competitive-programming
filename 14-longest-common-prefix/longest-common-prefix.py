class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Find the minimum length string
        min_len = min(len(s) for s in strs)
        
        # Use first string as reference
        first_str = strs[0]
        result = []
        
        # Check each character position
        for i in range(min_len):
            current_char = first_str[i]
            
            # Check if all strings have the same character at position i
            for j in range(1, len(strs)):  # Start from 1 since first string is reference
                if strs[j][i] != current_char:
                    return ''.join(result)
            
            result.append(current_char)
        
        return ''.join(result)
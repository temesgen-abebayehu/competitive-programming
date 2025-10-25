class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        max_common = min(len(s) for s in strs) # n - len of strs
        # create a variable 
        word = strs[0]
        count = [] # it counts the logenst common prefix

        # for loop that iterate to all strings in the strs
        for i in range(max_common):  # m len min string of strs
            for j in range(len(strs)): # n len strs
                if word[i] != strs[j][i]:
                    return ''.join(count)
            count.append(word[i])
        return ''.join(count)

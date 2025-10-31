class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in range(len(s)):
            # if stack is not empty and the last value equal to current value
            if stack and stack[-1][0] == s[i]:
                stack[-1][1] += 1

            # the neighbore are not similar
            else:
                stack.append([s[i],1])
                
            # if we got k consquative char simply remove it
            if stack and stack[-1][1] == k:
                stack.pop()
            

        result = []
        for ele in stack:
            result.append(ele[0] * ele[1])

        return ''.join(result)

            
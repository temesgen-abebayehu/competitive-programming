class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in range(len(s)):
            if stack and stack[-1][0] == s[i]:
                stack[-1][1] += 1
            else:
                stack.append([s[i],1])
                
            if stack and stack[-1][1] == k:
                stack.pop()
            


        result = []
        print(stack)
        for ele in stack:
            result.append(ele[0] * ele[1])

        return ''.join(result)

            
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = '({['

        count = 0
        for i in range(len(s)):
            if s[i] in p:
                stack.append(s[i])
                count += 1
            else:
                if stack and stack[-1] == '(' and s[i] == ')':
                    stack.pop()
                elif stack and stack[-1] == '{' and s[i] == '}':
                    stack.pop()
                elif stack and stack[-1] == '[' and s[i] == ']':
                    stack.pop()
                count -= 1

        if len(stack) == 0 and count == 0:
            return True
        else:
            return False

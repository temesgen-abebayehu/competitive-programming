class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = {'[', '{', '('}
        for b in s:
            if b in open:
                stack.append(b)
            else:
                if stack and ((stack[-1] == '{' and b == '}') or (stack[-1] == '[' and b == ']') or (stack[-1] == '(' and b == ')')):
                    stack.pop()
                else:
                    return False
        return not stack

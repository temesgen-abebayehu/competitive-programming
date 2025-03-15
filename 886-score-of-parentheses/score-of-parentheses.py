class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                top = stack.pop()
                if top == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2 * top
                    
        return stack[0]
                

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ('+', '-', '*','/')
        for i in tokens:
            if i in op:
                f = int(stack.pop())
                s = int(stack.pop())
                if i == '+':
                    stack.append(f+s)
                elif i == '-':
                    stack.append(s-f)
                elif i == '*':
                    stack.append(s*f)
                else:
                    result = s//f
                    if s*f < 0 and s%f !=0:
                        result += 1
                    stack.append(result)
                
            else:
                stack.append(i)
        return int(stack[0])
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char not in ['+','-','/','*']:
                stack.append(int(char))
            else:
                b = stack.pop()
                a = stack.pop()

                if char == '+':
                    result = a+b
                elif char == '-':
                    result = a-b
                elif char == '*':
                    result = a*b
                else:
                    result = int(a/b)
                stack.append(result)
        return stack[0]
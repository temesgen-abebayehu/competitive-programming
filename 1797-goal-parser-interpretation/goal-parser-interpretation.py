class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        tem_str = ''
        ans = ''

        for i in command:
            stack.append(i)
            if stack[-1] == 'G' or stack[-1] == ')':
                while stack:
                    tem_str += stack.pop()
            print(tem_str)
            if tem_str == 'G':
                ans += 'G'
                tem_str = ''
            elif tem_str == ')la(':
                ans += 'al'
                tem_str = ''
            elif tem_str == ')(':
                ans += 'o'
                tem_str = ''

        return ans
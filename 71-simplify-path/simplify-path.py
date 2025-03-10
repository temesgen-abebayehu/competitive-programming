class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        p = path.split('/')
        for s in p:
            if s == '..':
                if stack:
                    stack.pop()
            elif s and s != '.':
                stack.append(s)
        return '/'+'/'.join(stack)
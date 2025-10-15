class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for folder in path.split('/'):
            if folder == '' or folder == '.':
                continue
            if folder == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(folder)            

        return '/' + '/'.join(stack)
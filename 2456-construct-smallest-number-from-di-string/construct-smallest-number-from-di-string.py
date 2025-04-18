class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        res = []
        stack = []
        for i in range(n + 1):
            stack.append(str(i + 1))
            if i == n or pattern[i] == 'I':
                while stack:
                    res.append(stack.pop())
        return ''.join(res)
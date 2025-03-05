class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for p in logs:
            if stack and '..' in p:
                stack.pop()
            elif p[0] != '.':
                stack.append(p)
        return len(stack)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        for c in s:
            if not stack_s and c == '#':
                continue
            elif c == '#':
                stack_s.pop()
            else:
                stack_s.append(c)

        for c in t:
            if not stack_t and c == '#':
                continue
            elif stack_t and c == '#':
                stack_t.pop()
            else:
                stack_t.append(c)
        
        return True if stack_s == stack_t else False

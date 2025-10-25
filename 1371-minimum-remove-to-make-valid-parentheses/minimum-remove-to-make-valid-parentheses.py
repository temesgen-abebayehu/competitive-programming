class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # create set that hold the remove index
        remove = set()

        # iterate to iddentify invalid ')' left->right
        balance = 0
        for i in range(len(s)):
            if s[i] == '(':
                balance += 1
            elif s[i] == ')':
                if balance > 0:
                    balance -= 1
                else:
                    remove.add(i)
                    balance = 0
        # iterate to identify invalid '(' from right -> left
        balance = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                balance += 1
            elif s[i] == '(':
                if balance > 0:
                    balance -= 1
                else:
                    remove.add(i)
                    balance = 0

        # create a variable that contain result string
        result = []

        # iterate and pick valid character from string
        for i in range(len(s)):
            if i in remove:
                continue
            result.append(s[i])

        return ''.join(result)
            
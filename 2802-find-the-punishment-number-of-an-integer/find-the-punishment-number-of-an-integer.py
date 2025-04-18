class Solution:
    def punishmentNumber(self, n: int) -> int:
        if n == 0:
            return 0
        square = n*n
        if self.is_valid(n, str(square)):
            return square + self.punishmentNumber(n-1)
        else:
            return self.punishmentNumber(n-1)

    def is_valid(self, target, s):
        if not s:
            return target == 0

        for i in range(1, len(s) + 1):
            curr = int(s[:i])
            if self.is_valid(target - curr, s[i:]):
                return True
        return False

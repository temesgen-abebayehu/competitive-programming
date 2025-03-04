class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = sorted(s, reverse=True)
        s.remove('1')
        s.append('1')
        return ''.join(s)
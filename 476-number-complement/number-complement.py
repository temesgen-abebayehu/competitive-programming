class Solution:
    def findComplement(self, num: int) -> int:
        p = num.bit_length()
        return num ^ (2**p - 1)
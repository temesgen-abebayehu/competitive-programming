class Solution:
    def smallestNumber(self, n: int) -> int:
        l = n.bit_length()
        return 2**l-1
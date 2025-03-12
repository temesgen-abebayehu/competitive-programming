class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        Pre_symbol = self.kthGrammar(n-1, (k+1)//2)

        if k % 2 == 0:
            return 1 - Pre_symbol
        else:
            return Pre_symbol
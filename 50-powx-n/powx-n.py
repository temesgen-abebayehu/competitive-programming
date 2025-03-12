class Solution:
    def myPow(self, x: float, n: int) -> float:
        def powHelper(x, n):
            if n == 0:
                return 1

            half = powHelper(x, n//2)

            if n%2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            return 1/powHelper(x,-n)
        else:
            return powHelper(x,n)
            
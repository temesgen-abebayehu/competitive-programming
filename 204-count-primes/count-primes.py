class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime: list[bool] = [True for _ in range(n + 1)]
        i = 2
        res = 0
        while i  < n:
            if is_prime[i]:
                j = i * i
                res += 1
                while j < n:
                    is_prime[j] = False
                    j += i
            i += 1
        return res
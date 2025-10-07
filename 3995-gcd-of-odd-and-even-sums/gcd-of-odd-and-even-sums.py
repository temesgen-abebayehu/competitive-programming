class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        sumEven = 0
        j,k = 1, 2
        for i in range(n):
            sumOdd += j
            sumEven += k
            j += 2
            k += 2

        return math.gcd(sumOdd, sumEven)
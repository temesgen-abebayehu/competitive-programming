class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        memo = {} # memorization
        def dp(i):
            if i >= n:
                return 0

            if i in memo:
                return memo[i]

            memo[i] = energy[i] + dp(i+k)

            return memo[i]


        result = -inf
        for i in range(n):
            result = max(result, dp(i))

        return result
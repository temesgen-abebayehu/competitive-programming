class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        def dp(x):
            if x <= 1:
                return 0

            if x in memo:
                return memo[x]

            if x%2==0:
                memo[x] = 1 + dp(x//2)
            else:
                memo[x] = 1 + dp(3*x+1)
            return memo[x]

        nums = []
        for x in range(lo, hi+1):
            power = dp(x)
            nums.append((power, x))

        nums.sort()
        return nums[k-1][1]
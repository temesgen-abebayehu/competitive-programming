class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(i):
            if i < 0:
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + dp(i-2), dp(i-1))

            return memo[i]

        return dp(len(nums) - 1)
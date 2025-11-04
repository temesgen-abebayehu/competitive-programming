class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        def dp(i, last, memo):
            if i > last:
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + dp(i+2, last, memo), dp(i+1, last, memo))
            
            return memo[i]

        return max(dp(0, n-2, {}), dp(1, n-1, {}))
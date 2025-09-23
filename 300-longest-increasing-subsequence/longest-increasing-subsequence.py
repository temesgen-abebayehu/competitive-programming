class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [1] * n
        
        def dp(curr):
            if curr < 0:
                return

            for i in range(curr - 1, -1, -1):
                if nums[i] < nums[curr]:
                    memo[i] = max(memo[i], 1 + memo[curr])
            dp(curr - 1)
        dp(n - 1)
        return max(memo)
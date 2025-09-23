class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [1] * n
        for j in range(n - 1, -1, -1):
            for i in range(j - 1, -1, -1):
                if nums[i] < nums[j]:
                    memo[i] = max(memo[i], 1 + memo[j])
        return max(memo)
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        p_or = 0
        res = 0
        l = 0
        for r in range(n):
            while l < r and p_or & nums[r] != 0:
                p_or ^= nums[l]
                l += 1
            p_or |= nums[r]
            res = max(res, r-l+1)
        return res
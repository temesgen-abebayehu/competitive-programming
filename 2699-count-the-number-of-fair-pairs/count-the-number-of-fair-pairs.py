class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n):
            left = bisect.bisect_left(nums, lower - nums[i], i+1, n)
            right = bisect.bisect_right(nums, upper - nums[i], i+1, n)
            res += right - left
        return res
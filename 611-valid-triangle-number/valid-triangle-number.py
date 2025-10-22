class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                curr_sum = nums[i] + nums[j]
                idx = bisect_left(nums, curr_sum)
                count += max(0, (idx-j-1))

        return count
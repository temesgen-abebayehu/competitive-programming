class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        sums = 0
        min_num = float('inf')
        max_num = float('-inf')
        for i in range(len(nums)):
            sums += nums[i]
            if sums < min_num:
                min_num = sums
            if sums > max_num:
                max_num = sums
       
        return max(abs(max_num - min_num), abs(max_num), abs(min_num))
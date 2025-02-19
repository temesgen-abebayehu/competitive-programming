class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums=total=count=0
        for num in nums:
            sums += num
            total = max(total, sums)
            if sums < 0:
                sums = 0
            if num < 0:
                count += 1
        if count==len(nums):
            return max(nums)
        else:
            return total
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        last = nums[-1]
        pre = 0
        
        for i in range(len(nums)):
            suff = last - nums[i]
            if pre == suff:
                return i
                
            pre = nums[i]
        else:
            return -1
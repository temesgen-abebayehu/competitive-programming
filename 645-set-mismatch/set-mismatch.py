class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        while i < n:
            curr_num = nums[i] - 1
            if curr_num == i or curr_num + 1 == nums[curr_num]:
                i+=1
            else:
                nums[i], nums[curr_num] = nums[curr_num], nums[i]
        
        for i in range(n):
            if nums[i] != i+1:
                return [nums[i], i+1]
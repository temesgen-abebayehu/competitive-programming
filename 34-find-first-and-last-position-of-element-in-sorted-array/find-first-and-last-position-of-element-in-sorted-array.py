class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = -1
        ub = -1

        l = 0
        h = len(nums) - 1
        while l <= h:
            m = (l + h) // 2
            if nums[m] == target:
                lb = m
                h = m - 1
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                h = m - 1
        
        l = 0
        h = len(nums) - 1
        while l <= h:
            m = (l + h) // 2
            if nums[m] == target:
                ub = m
                l = m + 1
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                h = m - 1

        return [lb, ub]
        
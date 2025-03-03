class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        if n<3:
            return 0

        nums.sort(reverse=True)

        for i in range(n-2):            
            if nums[i+1] + nums[i+2] > nums[i]:
                return sum(nums[i:i+3])

        return 0

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * (max(nums) + 1)

        for c in nums:
            count[c] += 1

        n = 0
        for i in range(len(count)):
            for j in range(count[i]):
                nums[n] = i
                n += 1

        
        
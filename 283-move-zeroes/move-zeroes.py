class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return 

        left = 0
        right = 1

        while right < n:
            if nums[left] == 0 and nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1

            if left < n and nums[left] != 0:
                left += 1
            if right < n and (nums[right] == 0 or left == right):
                right += 1
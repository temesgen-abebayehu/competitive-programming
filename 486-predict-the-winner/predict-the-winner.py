class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(left, right):
            if left == right:
                return nums[left]
            opt_left = nums[left] - helper(left + 1, right)
            opt_right = nums[right] - helper(left, right - 1)
            return max(opt_left, opt_right)
        
        return helper(0, len(nums) - 1) >= 0
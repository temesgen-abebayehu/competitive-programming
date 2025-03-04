class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pre = 0
        curr = 0

        for i in range(len(nums)-1):
            pre = curr
            curr = max(nums[i], pre-1)            
            if curr == 0:
                return False
        return True
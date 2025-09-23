class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0

        for i in range(n):
            for j in range(n):
                if nums[j] - nums[i] > nums[i]:
                    break
                    
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    res = max(res, nums[i] ^ nums[j])

        return res
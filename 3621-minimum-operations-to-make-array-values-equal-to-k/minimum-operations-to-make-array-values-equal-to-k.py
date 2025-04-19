class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        unique = set(nums)
        count = 0
        for i in unique:
            if i > k:
                count += 1
            elif i < k:
                return -1
        return count
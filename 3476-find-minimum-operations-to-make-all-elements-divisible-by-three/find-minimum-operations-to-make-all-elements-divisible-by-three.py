class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            rem = n%3
            res += min(rem, 3-rem)
        return res
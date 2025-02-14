class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if set(nums) == {0} and k<1:
            return 0

        n = len(nums)
        l = 0
        r = 0
        count = k
        max_len = 1

        while l<n and r<n:
            if nums[r] == 0 and count > 0:
                count -= 1
                r += 1
            elif nums[l] == 0 and nums[r] == 0 and count == 0:
                count += 1
                l += 1
            elif nums[r] == 0 and count == 0:
                l += 1
            else:
                r += 1
            max_len = max(max_len, r-l)

        return max_len
        
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        rim = total % p

        if rim == 0:
            return 0

        prefix = {0: -1}
        curr_sum = 0
        min_length = len(nums)

        for i, num in enumerate(nums):
            curr_sum = (curr_sum + num) % p
            target = (curr_sum - rim + p) % p

            if target in prefix:
                min_length = min(min_length, i - prefix[target])

            prefix[curr_sum] = i

        return min_length if min_length < len(nums) else -1
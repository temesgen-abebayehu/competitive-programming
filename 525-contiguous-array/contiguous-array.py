class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = defaultdict(int)
        prefix[0] = -1
        max_len = 0
        sums = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                sums += 1
            else:
                sums -= 1

            if sums in prefix:
                max_len = max(max_len, i - prefix[sums])
            else:
                prefix[sums] = i
        return max_len
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        remove = 0
        leftover = 0
        for key, value in count.items():
            remove += value // 2
            leftover += value % 2
        return [remove, leftover]
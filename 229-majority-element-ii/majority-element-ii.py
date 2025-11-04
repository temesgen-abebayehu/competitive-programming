class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        freq = Counter(nums)

        for num in set(nums):
            if freq[num] > n//3:
                ans.append(num)

        return ans
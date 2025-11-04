class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        major_ele = nums[0]
        for num in nums:
            if freq[num] > freq[major_ele]:
                major_ele = num

        return major_ele
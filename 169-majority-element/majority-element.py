class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        condidate = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                condidate = nums[i]

            if condidate == nums[i]:
                count += 1
            else:
                count -= 1

        return condidate
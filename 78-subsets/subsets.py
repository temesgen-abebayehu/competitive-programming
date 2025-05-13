class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(1<<len(nums)):
            temp = []
            for j in range(len(nums)):
                if i & (1<<j) != 0:
                    temp.append(nums[j])

            res.append(temp)

        return res
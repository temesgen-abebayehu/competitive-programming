class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def backtrack(l, r):
            if l==r:
                self.ans.append(nums.copy())
                return
            for i in range(l, r):
                nums[l], nums[i] = nums[i], nums[l]
                backtrack(l+1, r)
                nums[l], nums[i] = nums[i], nums[l]
            return
        backtrack(0, len(nums))
        return self.ans
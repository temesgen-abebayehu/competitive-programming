class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        while i<n:
            curr_ele = nums[i] - 1
            if curr_ele == i or curr_ele + 1 == nums[curr_ele]:
                i+=1
            else:
                nums[i], nums[curr_ele] = nums[curr_ele], nums[i]
        print(nums)        
        ans = []
        for i in range(n):
            if i+1 != nums[i]:
                ans.append(i+1)
        return ans
                
class Solution:
    def largestNumber(self, nums: List[int]) -> str:        
        def max_num(num1, num2):
            first = str(num1) + str(num2)
            second = str(num2) + str(num1)
            if int(first) > int(second):
                return num1
            else:
                return num2

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if max_num(nums[i], nums[j]) == nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        ans = [str(n) for n in nums]
        return ''.join(ans) if ans[0] != '0' else '0'
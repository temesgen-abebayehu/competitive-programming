class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pro1 = 1
        pro2 = 1
        sufix = []
        prefix = []

        l = 0
        r = n - 1
        while l < n and r >=0:
            pro1 *= nums[l]
            pro2 *= nums[r]

            prefix.append(pro1)
            sufix.append(pro2)
            l += 1
            r -= 1
            
        nums[0] = sufix[n-2]
        l = 0
        for r in range(1, n):
            nums[r] = prefix[l]
            if n-r-2 >= 0:
                nums[r] *= sufix[n-r-2]
            l += 1

        return nums
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def isValidate(mid):
            dec = [0] * (len(nums) + 1)
            for i in range(mid):
                l,r,v = queries[i]
                dec[l] += v
                dec[r+1] -= v

            #prefix sum
            for i in range(1, len(dec)):
                dec[i] += dec[i-1]

            #checking
            for i in range(len(nums)):
                if nums[i] > dec[i]:
                    return False
            else:
                return True

        #binary search
        l = 0
        r = len(queries)
        while l<=r:
            m = (l+r)//2
            if isValidate(m):
                r = m - 1
            else:
                l = m + 1

        #if not possible       
        if l > len(queries):
            return -1
        #if posible
        return l
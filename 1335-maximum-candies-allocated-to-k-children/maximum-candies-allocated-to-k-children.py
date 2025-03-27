class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        #validater function
        def isValidate(mid):
            if mid == 0:
                return True
            no_candies = 0
            for i in range(len(candies)):
                no_candies += candies[i] // mid
            return no_candies >= k

        #binary search
        l = 0
        r = max(candies)
        while l <= r:
            m = (l+r)//2
            if isValidate(m):
                l = m + 1
            else:
                r = m - 1
        return r
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isGood(mid):
            currSum = 0
            count = 1

            for i in nums:
                if currSum + i <= mid:
                    currSum += i
                else:
                    count += 1
                    currSum = i
            return count <= k
        
        minBound = max(nums)
        maxBound = sum(nums)

        while minBound <= maxBound:
            mid = (minBound + maxBound) // 2
            if isGood(mid):
                maxBound = mid-1
            else:
                minBound = mid+1
        
        return minBound
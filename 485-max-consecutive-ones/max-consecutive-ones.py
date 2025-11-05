class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        max_one = 0
        for num in nums:
            if num == 1:
                max_one += 1
            else:
                max_one = 0
            ans = max(ans, max_one)
        
        return ans
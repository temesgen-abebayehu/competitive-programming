from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        ans = 0
        left = 0  
        last_min = -1  
        last_max = -1 
        invalid = -1 

        for right in range(n):           
            if nums[right] == minK:
                last_min = right
            if nums[right] == maxK:
                last_max = right

            if nums[right] < minK or nums[right] > maxK:
                invalid = right

            if last_min != -1 and last_max != -1:              
                start = max(invalid + 1, left)
                ans += max(0, min(last_min, last_max) - start + 1)

        return ans
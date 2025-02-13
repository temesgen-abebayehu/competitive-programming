from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() 
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2] 
        min_gap = abs(ans - target)  
        
        for i in range(n - 2): 
            l = i + 1
            r = n - 1
            
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                current_gap = abs(current_sum - target)
                
                if current_gap < min_gap:
                    ans = current_sum
                    min_gap = current_gap
                
                if current_sum < target:
                    l += 1
                else:
                    r -= 1
        
        return ans
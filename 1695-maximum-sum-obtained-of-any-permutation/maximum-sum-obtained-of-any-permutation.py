class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)
        max_num = len(nums) + 1
        
        prefix = [0] * (max_num + 1)
        for i, j in requests:
            prefix[i] += 1
            if j < len(prefix) - 1:
                prefix[j + 1] -= 1
        
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]

        prefix.sort(reverse=True)
        ans = 0
        for i in range(len(nums)):
            ans += (prefix[i] * nums[i])
                
        return ans%(10**9 + 7)
            
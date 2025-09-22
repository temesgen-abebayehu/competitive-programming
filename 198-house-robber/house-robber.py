class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        n = len(nums)
        
        @cache
        def dp(i):
            if i >= n:
                return 0
            
            # if i in memo:
            #     return memo[i]
            
            return max(nums[i] + dp(i+2), dp(i+1))
            
            # return memo[i]

        return dp(0)
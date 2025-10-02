class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # bottom-up dp
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target+1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i-num]

        return dp[target]

        
        # # top-down dp
        # memo = {}
        # def dp(curr_target):
        #     if curr_target == 0:
        #         return 1

        #     if curr_target < 0:
        #         return 0

        #     if curr_target in memo:
        #         return memo[curr_target]

        #     count = 0
        #     for num in nums:
        #         count += dp(curr_target - num)
            
        #     memo[curr_target] = count
        #     return count

        # return dp(target)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # top-down dp
        memo = {}
        def dp(curr_target):
            if curr_target == 0:
                return 1

            if curr_target < 0:
                return 0

            if curr_target in memo:
                return memo[curr_target]

            count = 0
            for num in nums:
                count += dp(curr_target - num)
            
            memo[curr_target] = count
            return count

        return dp(target)
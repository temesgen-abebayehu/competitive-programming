class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        half = total // 2
        memo = defaultdict(int)
        
        
        def dp(tar, i):
            if tar == half:
                return True

            if i >= len(nums) or tar > half:
                return False

            if (tar,i) in memo:
                return memo[(tar, i)]

  

            memo[(tar, i)] = dp(tar + nums[i], i+1) or dp(tar, i+1)
            return memo[(tar, i)]

        return dp(0,0)
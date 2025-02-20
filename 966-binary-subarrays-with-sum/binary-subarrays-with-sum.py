class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1

        sums = 0
        ans = 0
        for i in range(len(nums)):
            sums += nums[i]
            if sums - goal in count:
                ans += count[sums - goal]
            count[sums] += 1
        print(count)
        return ans
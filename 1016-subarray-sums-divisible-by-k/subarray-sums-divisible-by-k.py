class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        sums = 0
        ans = 0
        for i in range(len(nums)):
            sums += nums[i]
            remin = sums % k
            if remin in count:
                ans += count[remin]
            count[remin] += 1
        return ans
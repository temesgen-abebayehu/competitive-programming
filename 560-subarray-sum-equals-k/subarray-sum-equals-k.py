class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        sums = 0
        ans = 0
        
        for n in nums:
            sums += n
            if sums - k in count:
                ans += count[sums - k]

            count[sums] += 1
        return ans
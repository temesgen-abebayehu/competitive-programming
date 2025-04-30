class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        heapq.heapify(nums)
        while len(nums) > 1 and nums[0] < k:
            l = heapq.heappop(nums)
            r = heapq.heappop(nums)
            
            heapq.heappush(nums, l*2 + r)

            count += 1
        return count
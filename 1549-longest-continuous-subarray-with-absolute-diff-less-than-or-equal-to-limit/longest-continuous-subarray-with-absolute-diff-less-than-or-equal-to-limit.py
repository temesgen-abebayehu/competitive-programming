class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q = deque()
        max_q = deque()
        l = 0
        ans = 0
        for r, n in enumerate(nums):
            while min_q and nums[min_q[-1]] >= n:
                min_q.pop()
            min_q.append(r)
                
            while max_q and nums[max_q[-1]] <= n:
                max_q.pop()
            max_q.append(r)

            while nums[max_q[0]] - nums[min_q[0]] > limit:
                l += 1
                if min_q[0] < l:
                    min_q.popleft()
                if max_q[0] < l:
                    max_q.popleft()

            ans = max(ans, r-l+1)

        return ans
                
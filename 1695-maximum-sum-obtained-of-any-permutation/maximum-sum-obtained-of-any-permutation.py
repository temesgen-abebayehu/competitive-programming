class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)
        max_num = 0
        for i, j in requests:
            max_num = max(max_num, j)
        
        prefix = [0] * (max_num + 1)
        for i, j in requests:
            prefix[i] += 1
            if j < len(prefix) - 1:
                prefix[j + 1] -= 1
        
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]

        count = {}
        for idx, val in enumerate(prefix):
            if val > 0:
                count[idx] = val
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)

        arr = [0] * len(nums)
        i = 0
        for c in count:
            arr[c[0]] = nums[i]
            i += 1

        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]

        ans = 0
        for i, j in requests:
            ans += arr[j]
            if i > 0:
                ans -= arr[i - 1]
        return ans%(10**9 + 7)
            
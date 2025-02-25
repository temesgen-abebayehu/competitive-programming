class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        without_itself = []
        for i in range(n):
            if nums[i]%k == 0:
                if i-1>0 and nums[i-1]%k == 0:
                    without_itself.append(nums[i])
                elif i+1<n and nums[i+1]%k == 0:
                    without_itself.append(nums[i])
                else:
                    continue
            else:
                without_itself.append(nums[i])

        count = defaultdict(int)
        count[0] = 1
        sums = 0
        l = len(without_itself)
        for i in range(l):
            sums += without_itself[i]
            if sums%k in count:
                return True
            count[sums%k] += 1
        return False
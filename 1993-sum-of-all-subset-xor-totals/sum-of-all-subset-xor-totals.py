class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sub_set = []
        for i in range(2**len(nums)):
            arr = []
            for j in range(len(nums)-1, -1,-1):
                if i>>j & 1:
                    arr.append(nums[j])

            if len(arr) > 0:
                sub_set.append(arr)

        ans = 0
        print(sub_set)
        for arr in sub_set:
            curr = arr[0]
            for i in range(1, len(arr)):
                curr ^= arr[i]
            ans += curr
        return ans
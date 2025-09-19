class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        nums  = []
        for i in range(n):
            nums.append(nums1[i] - nums2[i])

        pairs = 0

        def merge(left, right):
            nonlocal pairs
            ln = len(left)
            rn = len(right)

            # count pairs
            j = 0
            for i in range(ln):
                while j<rn and left[i] - right[j] > diff:
                    j+=1
                pairs += (rn-j)

            result = []
            l,r = 0, 0
            while l < ln and r < rn:
                if left[l] < right[r]:
                    result.append(left[l])
                    l+=1
                else:
                    result.append(right[r])
                    r+=1

            result.extend(left[l:])
            result.extend(right[r:])

            return result

        def divide(arr):
            n = len(arr)
            m = n//2

            if n <= 1:
                return arr

            left = divide(arr[:m])
            right = divide(arr[m:])

            return merge(left,right)

        divide(nums)
        return pairs


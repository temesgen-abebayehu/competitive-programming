class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        triangles = 0
        for k in range(n-1, -1, -1):
            i, j = 0, k-1
            while i<j:
                if nums[i] + nums[j] > nums[k]:
                    triangles += (j-i)
                    j-=1
                else:
                    i+=1


        return triangles
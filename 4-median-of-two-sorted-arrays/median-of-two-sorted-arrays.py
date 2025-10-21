class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        i,j = 0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                i+=1
            else:
                arr.append(nums2[j])
                j+=1

        if nums1:
            arr.extend(nums1[i:])
        if nums2:
            arr.extend(nums2[j:])

        mid = len(arr)//2
        if len(arr)%2==0:
            return (arr[mid - 1] + arr[mid])/2
        else:
            return arr[mid]

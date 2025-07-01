class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1  = 0
        for i in nums1:
            xor1 ^= i
        
        xor2 = 0
        for j in  nums2:
            xor2 ^= j

        num1_result = xor1 if len(nums2) % 2 == 1 else 0
        num2_result = xor2 if len(nums1) % 2 == 1 else 0
        
        return num1_result ^ num2_result
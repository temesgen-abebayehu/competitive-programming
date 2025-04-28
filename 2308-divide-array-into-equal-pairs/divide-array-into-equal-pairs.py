class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dic = Counter(nums)
        for i in dic:
            if dic[i] % 2 != 0:
                return False
        return True
        
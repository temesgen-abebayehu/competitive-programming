class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product = defaultdict(int)
        ans = 0

        # add the product to dictionary
        for first in range(len(nums)):
            for second in range(first + 1, len(nums)):
                product[nums[first] * nums[second]] += 1

        # cout the valid tuples
        for key, value in product.items():
            if value > 1:
                ans += (value*(value - 1)//2) * 8

        return ans
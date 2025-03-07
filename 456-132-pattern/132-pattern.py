class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        min_n = nums[0]
        for num in nums[1:]:
            while stack and num >= stack[-1][0]:
                stack.pop()
            if stack and num > stack[-1][1]:
                return True

            stack.append([num, min_n])
            min_n = min(min_n, num)

        return False
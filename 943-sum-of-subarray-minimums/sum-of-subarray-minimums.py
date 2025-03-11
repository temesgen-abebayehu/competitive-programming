class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        sums = 0
        ans = 0

        for i, v in enumerate(arr):
            count = 1
            while stack and stack[-1][0] > v:
                a, b = stack.pop()
                sums -= (a * b)
                count += b

            stack.append((v, count))
            sums += (v * count)
            ans += sums

        return ans % (10**9 + 7)
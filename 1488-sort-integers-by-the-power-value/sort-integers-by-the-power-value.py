class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}

        def count_power(num):
            if num == 1:
                return 1

            if num in memo:
                return memo[num]

            
            if num % 2 == 0:
                memo[num] = 1 + count_power(num//2)
            else:
                memo[num] = 1 + count_power(3 * num + 1)

            return memo[num]

        ans = []
        for num in range(lo, hi+1):
            ans.append((count_power(num), num))

        ans.sort(key=lambda x: (x[0], x[1]))
        return ans[k-1][1]
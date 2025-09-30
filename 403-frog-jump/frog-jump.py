class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        s = defaultdict(int)
        for i, v in enumerate(stones):
            s[v] = i

        memo = {}

        if 1 not in s:
            return False

        def dp(i, k):
            if i >= n or k == 0:
                return False
            if i == n-1:
                return True
            
            state = (i, k)
            if state in memo:
                return memo[state]

            res = False
            if stones[i] + k-1 in s:
                res = dp(s[stones[i] + k-1],  k-1)
            if stones[i] + k in s:
                res = res or dp(s[stones[i] + k], k)
            if stones[i] + k+1 in s:
                res = res or dp(s[stones[i] + k+1], k+1)

            memo[state] = res
            return res

        return dp(1, 1)
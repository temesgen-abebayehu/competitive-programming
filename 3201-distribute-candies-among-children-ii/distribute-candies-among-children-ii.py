class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        total = math.comb(n+2, 2)

        one_child = 0
        if n-limit+1 >= 2:
            one_child = math.comb(n-limit+1, 2) * 3

        two_child = 0
        if n-2*limit >= 2:
            two_child = math.comb(n-2*limit, 2) * 3

        three_child = 0
        if n-3*limit-1 >=2:
            three_child = math.comb(n-3*limit-1, 2)

        ans = total - one_child + two_child - three_child
        return ans

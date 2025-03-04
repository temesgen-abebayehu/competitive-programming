class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_R = 0
        count_L = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == 'L':
                count_L += 1
            else:
                count_R += 1

            if count_L == count_R:
                count_L = 0
                count_R = 0
                ans += 1

        return ans
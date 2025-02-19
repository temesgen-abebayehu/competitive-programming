class Solution:
    def maxScore(self, s: str) -> int:
        count = Counter(s)
        left = right = ans = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                left += 1
            else:
                right += 1
            print(left, right, ans)
            ans = max(ans, left + (count['1'] - right))
        return ans
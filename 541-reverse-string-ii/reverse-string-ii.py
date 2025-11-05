class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        char_list = list(s)

        for i in range(0, n, 2*k):
            left = i
            right = min(n-1, i + k - 1)
            while left < right:
                char_list[left], char_list[right] = char_list[right], char_list[left]
                left += 1
                right -= 1

        return ''.join(char_list)
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * 50001
        
        # add cut point
        for i, j, d in shifts:
            if d == 0:
                prefix[i] += -1
                if j < 50001:
                    prefix[j + 1] += 1
            else:
                prefix[i] += 1
                if j < 50001:
                    prefix[j + 1] += -1

        # sum each
        for i in range(1, 50001):
            prefix[i] += prefix[i - 1]
        
        # operate shift
        ans = []

        for i in range(len(s)):
            c = ((ord(s[i]) - 97) + prefix[i]) % 26
            ans.append(chr(c + 97))
        
        return ''.join(ans)
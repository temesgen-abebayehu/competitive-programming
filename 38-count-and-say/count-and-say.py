class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'

        for i in range(1, n):
            result = []
            count = 1
            for j in range(1, len(s)):
                if s[j] == s[j-1]:
                    count += 1
                else:
                    result.append(str(count) + s[j-1])
                    count = 1
            result.append(str(count)+s[-1])
            s = ''.join(result)
        return s
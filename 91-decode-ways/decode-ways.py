class Solution:
    def numDecodings(self, s: str) -> int:
        docode = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26'}

        memo = {}
        def dp(i):
            if i == len(s) - 1 and s[i] != '0':
                return 1
            if i > len(s)-1:
                return 1
                
            if i in memo:
                return memo[i]
            res = 0
            if s[i] in docode:
                res += dp(i+1)
            if s[i:i+2] in docode:
                res += dp(i+2)

            memo[i] = res
            return res
        return dp(0)



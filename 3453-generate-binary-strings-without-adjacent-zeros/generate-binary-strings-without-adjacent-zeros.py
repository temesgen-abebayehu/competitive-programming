class Solution:
    def validStrings(self, n: int) -> List[str]:
        self.ans = []
        def backtrack(s,n,l):
            if l==n:
                count = 0
                for c in s:
                    if c == '0':
                        count += 1
                    else:
                        count = 0
                    if count == 2:
                        break
                if count < 2:
                    self.ans.append(s)
                s=''
                return
            
            backtrack(s+'1', n, l+1)
            backtrack(s+'0', n, l+1)
            return 
        backtrack('', n, 0)
        return self.ans
            
class Solution:
    def validStrings(self, n: int) -> List[str]:
        self.ans = []
        def backtrack(s,n,l):
            if l==n:                
                self.ans.append(s)
                s=''
                return
            
            backtrack(s+'1', n, l+1)
            if s and s[-1] == '0':
                return
            backtrack(s+'0', n, l+1)
            return 
        backtrack('', n, 0)
        return self.ans
            
class Solution:
    def validStrings(self, n: int) -> List[str]:
        self.ans = []
        def backtrack(s,n):
            if len(s)==n:                
                self.ans.append(s)
                s=''
                return
            
            backtrack(s+'1', n)
            if s and s[-1] == '0':
                return
            backtrack(s+'0', n)
            return 
        backtrack('', n)
        return self.ans
            
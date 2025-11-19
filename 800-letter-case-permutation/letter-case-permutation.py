class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        def permutaion(i, p):
            if i == len(s):
                ans.append(''.join(p))
                return 

            if s[i].isdigit():
                permutaion(i+1, p + [s[i]])
            else:
                permutaion(i+1, p + [s[i].lower()])
                permutaion(i+1, p + [s[i].upper()])
        
        ans = []
        permutaion(0, [])
        return ans
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)
        
        if k > n:
            return False
        
        count_s1 = Counter(s1)
        count_s2 = Counter(s2[:k])        

        if count_s2 == count_s1:
            return True

        l = 0
        for r in range(k, n):
            count_s2[s2[r]] += 1
            
            count_s2[s2[l]] -= 1
            if count_s2[s2[l]] == 0:
                del count_s2[s2[l]]
            
            l += 1
            
            if count_s2 == count_s1:
                return True

        return False
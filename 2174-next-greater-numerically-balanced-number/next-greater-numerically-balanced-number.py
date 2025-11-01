from itertools import permutations

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        length = len(str(n))
        result = float('inf')
        
        # Define combinations for each length
        combos = {
            1: [[1]],
            2: [[2,2]],
            3: [[1,2,2], [3,3,3]],
            4: [[1,3,3,3], [4,4,4,4]],
            5: [[1,4,4,4,4], [2,2,3,3,3], [5,5,5,5,5]],
            6: [[1,2,2,3,3,3], [1,5,5,5,5,5], [2,2,4,4,4,4], [6,6,6,6,6,6]],
            7: [[1,2,2,4,4,4,4]]
        }
        
        # Check length n
        if length in combos:
            for combo in combos[length]:
                for perm in set(permutations(combo)):
                    num = int(''.join(map(str, perm)))
                    if num > n:
                        result = min(result, num)
        
        # Check length n+1
        if length + 1 in combos:
            for combo in combos[length + 1]:
                for perm in set(permutations(combo)):
                    num = int(''.join(map(str, perm)))
                    result = min(result, num)
        
        return result
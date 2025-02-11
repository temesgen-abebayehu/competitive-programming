class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        
        target = [tuple(row) for row in target]
            
        
        for _ in range(3):
            mat = list(zip(*mat))
            mat = [row[::-1] for row in mat]
            print(mat)
            print('---------')
            if mat == target:
                return True
        else:
            return False
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if not edges and n == 1:
            return 0

        outdoor = set()
        indoor = set()
        for o, e in edges:
            outdoor.add(o)
            indoor.add(e)

        for i in range(n):
            if i not in indoor or i not in outdoor:
                outdoor.add(i)
        strong = []
        for o in outdoor:
            if o not in indoor:
                strong.append(o)

        if len(strong) == 1:
            return strong[0]
        else:
            return -1
        

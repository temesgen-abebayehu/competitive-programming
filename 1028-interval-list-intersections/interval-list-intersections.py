class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n = len(firstList)
        m = len(secondList)
        if n==0 or m==0:
            return []

        intersection = []

        for i in range(n):
            for j in range(m):                
                lower = max(firstList[i][0], secondList[j][0])
                upper = min(firstList[i][1], secondList[j][1])
                if lower <= upper:
                    intersection.append([lower, upper])

        return intersection
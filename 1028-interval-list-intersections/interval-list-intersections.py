class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n = len(firstList)
        m = len(secondList)
        if n==0 or m==0:
            return []

        intersection = []

        l = 0
        r = 0
        while l<n and r<m:               
            lower = max(firstList[l][0], secondList[r][0])
            upper = min(firstList[l][1], secondList[r][1])
            if lower <= upper:
                intersection.append([lower, upper])
                
            if firstList[l][1] < secondList[r][1]:
                l += 1
            else:
                r += 1

        return intersection
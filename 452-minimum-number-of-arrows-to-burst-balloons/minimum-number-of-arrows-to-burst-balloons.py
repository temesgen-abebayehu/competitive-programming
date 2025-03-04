class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrow = 1
        curr = points[0][1]
        for i in range(len(points)-1):
            if curr < points[i + 1][0]:
                arrow += 1
                curr = points[i + 1][1]
            else:
                if curr > points[i + 1][1]:
                    curr = points[i + 1][1]
        return arrow
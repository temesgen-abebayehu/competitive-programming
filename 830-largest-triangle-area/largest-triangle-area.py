class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        ans = 0
        for s1 in range(n):
            for s2 in range(s1+1, n):
                for s3 in range(s2+1, n):
                    area = 0.5 * abs(
                        points[s1][0]*(points[s2][1] - points[s3][1]) + 
                        points[s2][0]*(points[s3][1] - points[s1][1]) + 
                        points[s3][0]*(points[s1][1] - points[s2][1]))
                    ans = max(ans, area)

        return ans
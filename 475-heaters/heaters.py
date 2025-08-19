class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        radius = 0

        for h in houses:
            pos = bisect.bisect_left(heaters, h)
            r1, r2 = float('inf'), float('inf')
            if pos > 0:
                r1 = abs(h - heaters[pos-1])
            if pos < len(heaters):
                r2 = abs(h - heaters[pos])
            dis = min(r1, r2)
            radius = max(radius, dis)
        
        return radius
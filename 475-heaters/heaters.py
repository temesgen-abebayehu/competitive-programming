class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        pos = 0
        radius = 0

        for h in houses:
            while pos + 1 < len(heaters) and heaters[pos+1] < h:
                pos += 1

            r1 = abs(heaters[pos] - h)
            r2 = float('inf')

            if pos + 1 < len(heaters):
                r2 = abs(heaters[pos + 1] - h)

            dis = min(r1,r2)
            radius = max(radius, dis)
        
        return radius
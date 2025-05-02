class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        used = []
        i = 0
        for i in range(1, n):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                if len(used) < ladders:
                    heappush(used, diff)
                else:
                    cost = heappushpop(used, diff)
                    if bricks >= cost:
                        bricks -= cost                        
                    else:
                        return i - 1
        return i
                    
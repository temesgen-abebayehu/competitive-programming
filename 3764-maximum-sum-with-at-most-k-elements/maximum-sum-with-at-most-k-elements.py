class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:        
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                grid[i][j] = -grid[i][j]

        max_num = []
        for i in range(n):
            heapq.heapify(grid[i])
            for _ in range(limits[i]):
                mx = -(heapq.heappop(grid[i]))
                if len(max_num) < k:
                    heapq.heappush(max_num, mx)
                else:
                    heapq.heappushpop(max_num, mx)

        return sum(max_num)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        row = len(grid)
        col = len(grid[0])

        def binary_search(arr):
            l = 0
            r = col - 1
            while l <= r:
                m = (l+r)//2
                if arr[m] < 0:
                    r = m-1
                else:
                    l=m+1
            return l

        for arr in grid:
            pos = binary_search(arr)
            ans += col - pos

        return ans
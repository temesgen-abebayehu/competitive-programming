class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l = 0
        r = n-1
        while l<=r:
            m = (l+r)//2
            if citations[m] < (n - m):
                l = m + 1
            else:
                r = m - 1
        return n - l
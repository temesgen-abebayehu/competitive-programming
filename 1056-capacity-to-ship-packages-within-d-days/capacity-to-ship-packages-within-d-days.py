class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isValidate(needed):
            sums = 0
            d = 1
            for w in weights:
                sums += w
                if sums > needed:
                    d += 1
                    sums = w
            return d <= days
        
        l = max(weights)
        r = sum(weights)
        while l <= r:
            m = (l+r)//2
            if isValidate(m):
                r = m - 1
            else:
                l = m + 1
                
        return l
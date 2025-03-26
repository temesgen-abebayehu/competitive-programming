class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def isValidate(needed):
            no_car = 0
            for r in ranks:
                x = needed//r
                no_car += floor(sqrt(x))
            if no_car >= cars:
                return True
            else:
                return False

        #binary search
        l = min(ranks)    
        r = min(ranks) * cars * cars

        while l <= r:
            m = (l+r)//2
            if isValidate(m):
                r = m - 1
            else:
                l = m + 1
                
        return l
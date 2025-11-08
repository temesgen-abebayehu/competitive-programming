class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        sorted_cost = sorted(costs, key=lambda x: (x[0]-x[1]))

        count = 0
        result = 0
        
        for ca, cb in sorted_cost:
            if count < n//2:
                result += ca
                count += 1
            else:
                result += cb

        return result


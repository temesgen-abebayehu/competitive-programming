class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        sorted_cost = sorted(costs, key=lambda x: abs(x[0]-x[1]), reverse=True)

        counta = 0
        countb = 0
        result = 0
        
        for ca, cb in sorted_cost:
            if (ca < cb and counta < n//2):
                counta += 1
                result += ca

            elif cb < ca and countb < n//2:
                countb += 1
                result += cb

            elif counta < n//2:
                counta += 1
                result += ca

            elif countb < n//2:
                countb += 1
                result += cb

        return result


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        diff = []
        for i, (v1,v2) in enumerate(costs):
            diff.append([abs(v1-v2), i])

        diff.sort(reverse=True)
        counta = 0
        countb = 0
        result = 0
        
        for _, i in diff:
            if costs[i][0] < costs[i][1] and counta < n//2:
                counta += 1
                result += costs[i][0]

            elif costs[i][1] < costs[i][0] and countb < n//2:
                countb += 1
                result += costs[i][1]

            elif counta < n//2:
                counta += 1
                result += costs[i][0]

            elif countb < n//2:
                countb += 1
                result += costs[i][1]

            print(counta, countb)

        return result


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        city = defaultdict(int)
        for i in range(n):
            city[i] = costs[i][1] - costs[i][0]

        city = sorted(city.items(), key=lambda x: x[1])
        print(city)
        print(city[0][0])
        a = n//2
        min_cost = 0
        for b in range(n//2):
            min_cost += costs[city[b][0]][1] + costs[city[a][0]][0]
            a += 1
        return min_cost
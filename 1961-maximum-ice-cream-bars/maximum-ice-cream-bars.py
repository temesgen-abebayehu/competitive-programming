class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = [0] * (max(costs) + 1)

        for c in costs:
            count[c] += 1
        
        result = 0
        for i in range(len(count)):
            for j in range(count[i]):
                if i <= coins:
                    result += 1
                    coins -= i
                else:
                    return result
        return result
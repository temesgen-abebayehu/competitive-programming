class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = defaultdict(int)
        count[5] = 0
        count[10] = 0
        count[20] = 0

        for i in bills:
            if i == 5:
                count[5] += 1
            elif i==10:
                count[5] -= 1
                if count[5] == -1:
                    return False
                count[10] += 1
            else:
                if count[10] > 0:
                    count[10] -= 1
                    count[5] -= 1
                else:
                    count[5] -= 3
                
                if count[10] < 0 or count[5] < 0:
                    return False
                count[20] += 1
        return True
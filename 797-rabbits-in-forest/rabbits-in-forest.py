class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        
        total = 0
        for k, v in count.items():
            group = ceil(v/(k+1))
            total += group * (k + 1)

        return total
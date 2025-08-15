class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        pre = 0
        res = 0
        answers.sort()
        for i in range(len(answers)):
            if pre == 0:
                res += answers[i] + 1
                pre = answers[i]
            elif pre != 0 and answers[i] != answers[i-1]:
                res += answers[i] + 1
                pre = answers[i]
            else:
                pre -= 1
        return res
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c_one = Counter(word1)
        c_two = Counter(word2)

        res = set()
        for l in c_one:
            res.add(abs(c_one[l] - c_two[l]))
        for l in c_two:
            res.add(abs(c_two[l] - c_one[l]))
        
        for i in res:
            if i > 3:
                return False
        return True
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        paper = [0] * (max(citations) + 1)
        for c in citations :
            paper[c] += 1

        total = 0
        for i in range(len(paper)-1, -1, -1):
            total += paper[i]
            if total >= i:
                return i            
        else:
            return 0
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        que = deque()

        for d in deck:
            if que:
                back = que.pop()
                que.appendleft(back)
            que.appendleft(d)
        return list(que)
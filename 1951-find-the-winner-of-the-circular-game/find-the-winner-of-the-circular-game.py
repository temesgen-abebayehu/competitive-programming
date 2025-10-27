class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque(range(1,n+1))
        while len(queue) > 1:
            queue.rotate(-(k-1))
            queue.popleft()

        return queue[0]
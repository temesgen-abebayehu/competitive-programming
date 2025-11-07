class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'

        queue = deque()
        for digit in num:
            while queue and queue[-1] > digit and k > 0:
                queue.pop()
                k-=1

            queue.append(digit)

        while queue and k > 0:
            queue.pop()
            k-=1
        while queue and queue[0] == '0':
            queue.popleft()

        if len(queue) == 0:
            return '0'

        return ''.join(queue)
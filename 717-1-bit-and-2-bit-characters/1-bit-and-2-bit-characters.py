class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        deq = deque(bits)
        while len(deq) > 1:
            if deq[0] == 1:
                deq.popleft()
                deq.popleft()
            else:
                deq.popleft()
        if not deq:
            return False
        else:
            return True
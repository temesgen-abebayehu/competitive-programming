class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        move = 0
        while maxDoubles > 0 and target > 1:
            if target%2 == 1:
                move += 2
                target = (target - 1) // 2
            else:
                move += 1
                target //= 2
            maxDoubles -= 1

        return move + target - 1
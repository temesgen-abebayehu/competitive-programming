class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def isValidate(mid):
            count_day = 1
            left = 0
            for right in range(1, len(position)):
                if position[right] - position[left] >= mid:
                    count_day += 1
                    left = right
            return count_day >= m

        #binary search
        l = 1
        r = position[-1] - position[0]
        while l<=r:
            mid = (l+r)//2
            if isValidate(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        res = [0]*k
        for i in arr:
            res[i%k] += 1
        if k%2 == 0 and res[k//2] % 2 == 1:
            return False

        for i in range(k//2 + 1):
            if res[i] != res[-i%k]:
                return False
        return True
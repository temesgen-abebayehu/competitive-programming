class Solution:
    def minChanges(self, n: int, k: int) -> int:
        n_bit = bin(n)[2:]
        k_bit = bin(k)[2:]
        if len(k_bit) > len(n_bit):
            return -1
        
        k_bit = k_bit.zfill(len(n_bit))
        ans = 0
        for x, y in zip(n_bit, k_bit):
            if x != y:
                if x == '0':
                    return -1
                else:
                    ans += 1

        return ans
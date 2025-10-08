class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def count_divisor(num, a,b,c):
            counta = num//a
            countb = num//b
            countc = num//c

            lcm_ab = num//math.lcm(a,b)
            lcm_ac = num//math.lcm(a,c)
            lcm_bc = num//math.lcm(c,b)

            count_abc = math.lcm(math.lcm(a,b), c)
            lcm_abc = count_abc if count_abc == 0 else num//count_abc
            


            return counta + countb + countc - lcm_ab - lcm_ac - lcm_bc + lcm_abc

        l = 0
        r = 2*10**18
        ans = r
        
        while l <= r:
            m = (l+r)//2
            if count_divisor(m, a,b,c) >= n:
                ans = m
                r = m-1
            else:
                l = m+1

        return ans
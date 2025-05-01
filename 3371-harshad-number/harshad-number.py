class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digit = str(x)
        sum_x = 0
        for i in digit:
            sum_x += int(i)
        
        if x%sum_x == 0:
            return sum_x
        else:
            return -1
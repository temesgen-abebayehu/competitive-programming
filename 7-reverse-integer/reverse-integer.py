class Solution:
    def reverse(self, x: int) -> int:
        value = list(str(x))
        
        if value[0] == '-':
            result = -1 * int(''.join(reversed(value[1:])))
            return  result if result.bit_length()<=31 else 0
        else:
            result = int(''.join(reversed(value)))
            return result if result.bit_length()<=31 else 0
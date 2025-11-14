class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        rows = len(bank)
        cols = len(bank[0])

        ways = []
        for row in range(rows):
            way = 0
            for col in range(cols):
                if bank[row][col] == '1':
                    way += 1
            if way > 0:
                ways.append(way)

        ans = 0
        if len(ways) > 1:
            for i in range(1, len(ways)):
                ans += ways[i-1]  * ways[i]
        return ans
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = [set() for _ in range(9)]
        col_check = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != '.':
                    box_index = (row//3) * 3 + (col//3)
                    if (num in row_check[row]) or (num in col_check[col]) or (num in box[box_index]):

                        return False   
                                             
                    row_check[row].add(num)
                    col_check[col].add(num)
                    box[box_index].add(num)

        else:
            return True
                
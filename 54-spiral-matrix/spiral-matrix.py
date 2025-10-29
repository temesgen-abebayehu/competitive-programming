class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        ans = []

        while top <= bottom and left <= right:
            # left -> right
            for t in range(left, right + 1):
                ans.append(matrix[top][t])
            top += 1
            
            # top -> bottom
            for r in range(top, bottom + 1):
                ans.append(matrix[r][right])
            right -= 1
            
            # Check if we still have rows to traverse
            if top <= bottom:
                # right -> left   
                for l in range(right, left - 1, -1):
                    ans.append(matrix[bottom][l])
                bottom -= 1
            
            # Check if we still have columns to traverse
            if left <= right:
                # bottom -> top
                for b in range(bottom, top - 1, -1):
                    ans.append(matrix[b][left])
                left += 1

        return ans
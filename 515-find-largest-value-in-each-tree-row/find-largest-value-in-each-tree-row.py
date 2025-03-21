# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        row = deque([root])
        while row:
            level = len(row)
            max_val = float('-inf')
            for _ in range(level):
                node = row.popleft()
                max_val = max(max_val, node.val)

                if node.left:
                    row.append(node.left)
                if node.right:
                    row.append(node.right)

            ans.append(max_val)
            
        return ans
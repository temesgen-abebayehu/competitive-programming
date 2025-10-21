# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, minv, maxv):
            if not node:
                return True

            if node.val <= minv or node.val >= maxv:
                return False

            left = dfs(node.left, minv, node.val)
            right = dfs(node.right, node.val, maxv)

            return left and right


        return dfs(root, float('-inf'), float('inf'))
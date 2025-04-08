# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, min_v, max_v):
            if  not node:
                return max_v - min_v

            min_v = min(min_v, node.val)
            max_v = max(max_v, node.val)

            left_v = dfs(node.left, min_v, max_v)
            right_v = dfs(node.right, min_v, max_v)

            return max(left_v, right_v)

        return dfs(root, root.val, root.val)

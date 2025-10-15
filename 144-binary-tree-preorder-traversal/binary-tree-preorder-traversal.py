# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return 
            ans.append(node.val)
            if node.left:
                dfs(node.left)

            if node.right:
                dfs(node.right)

        ans = []
        dfs(root)
        return ans
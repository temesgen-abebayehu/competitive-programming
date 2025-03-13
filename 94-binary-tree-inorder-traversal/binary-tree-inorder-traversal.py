# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def preOrder(root):
            if root:
                preOrder(root.left)
                ans.append(root.val)
                preOrder(root.right)
        
        preOrder(root)
        return ans
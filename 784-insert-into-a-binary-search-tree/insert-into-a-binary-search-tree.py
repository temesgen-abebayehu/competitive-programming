# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        curr = TreeNode(val)
        def bst(root):     
            if root.val > val:
                if not root.left:                    
                    root.left = curr
                    return 

                bst(root.left)
                
            elif root.val < val:
                if not root.right:
                    root.right = curr
                    return 
                    
                bst(root.right)

        bst(root)
        return root

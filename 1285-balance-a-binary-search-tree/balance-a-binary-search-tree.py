# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def to_arr(node):
            if not node:
                return
            to_arr(node.left)
            arr.append(node.val)
            to_arr(node.right)

        to_arr(root)

        def constructor(l, r):
            if l > r:
                return None

            m = (l+r)//2
            node = TreeNode(arr[m])
            node.left = constructor(l, m-1)
            node.right = constructor(m+1, r)
            return node

        return constructor(0, len(arr)-1)
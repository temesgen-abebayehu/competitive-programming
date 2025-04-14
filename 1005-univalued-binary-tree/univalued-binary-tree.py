# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        que = deque()
        que.append(root)

        while que:
            n = len(que)
            for i in range(n):
                pre = que.popleft()

                if pre.left:
                    if pre.val != pre.left.val:
                        return False

                    que.append(pre.left)

                if pre.right:
                    if pre.val != pre.right.val:
                        return False

                    que.append(pre.right)
            
        return True
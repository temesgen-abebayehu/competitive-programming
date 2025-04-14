# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        curr = root
        que = deque()
        que.append(root)

        while que:
            n = len(que)
            for i in range(n):
                pre = que.popleft()
                if pre.left and pre.right:
                    if pre.val != pre.left.val or pre.val != pre.right.val:
                        return False

                    que.append(pre.left)
                    que.append(pre.right)

                elif pre.left:
                    if pre.val != pre.left.val:
                        return False

                    que.append(pre.left)

                elif pre.right:
                    if pre.val != pre.right.val:
                        return False

                    que.append(pre.right)
            
        return True
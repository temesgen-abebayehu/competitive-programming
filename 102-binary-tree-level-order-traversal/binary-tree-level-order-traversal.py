# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = [[root.val]]
        que = deque()
        que.append(root)
        while que:
            level = []
            n = len(que)
            for i in range(n):
                pre = que.popleft()

                if pre.left:
                    level.append(pre.left.val)
                    que.append(pre.left)

                if pre.right:
                    level.append(pre.right.val)
                    que.append(pre.right)

            if level:
                ans.append(level)
        return ans
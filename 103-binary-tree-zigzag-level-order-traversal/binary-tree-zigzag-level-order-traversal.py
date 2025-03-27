# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        level = 1
        que = deque([root])

        while que:
            temp = []
            for _ in range(len(que)):
                node = que.popleft()
                temp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            if level % 2 == 0:
                temp.reverse()
                ans.append(temp)
            else:
                ans.append(temp)
            level += 1
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node):
            if not node:
                return (0,0)
            l_sum, l_count = dfs(node.left)
            r_sum, r_count = dfs(node.right)

            total = l_sum + r_sum + node.val
            n = l_count + r_count + 1
            av = total // n
            if node.val == av:
                self.count += 1
            return (total, n)
        dfs(root)
        return self.count
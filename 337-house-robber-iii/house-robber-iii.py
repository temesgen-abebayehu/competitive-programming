# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dp(node, rob):
            if not node:
                return 0

            if (node, rob) in memo:
                return memo[(node, rob)]

            # not take
            res = max(dp(node.left, rob), dp(node.right, rob))

            # take
            if rob:
                res = node.val + dp(node.left, not rob) + dp(node.right, not rob)
            else:
                left_house = max(dp(node.left, not rob), dp(node.left, rob))
                right_house = max(dp(node.right, not rob), dp(node.right,rob))
                res = left_house + right_house

            memo[(node, rob)] = res
            return res

        return max(dp(root, False), dp(root, True))
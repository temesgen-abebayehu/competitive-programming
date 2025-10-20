# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        deq = deque()
        deq.append(root)
        ans = [root.val]

        while deq:
            for i in range(len(deq)):
                root = deq.popleft()
                if root.left:
                    deq.append(root.left)

                if root.right:
                    deq.append(root.right)

            if deq:
                ans.append(deq[-1].val)

        return ans
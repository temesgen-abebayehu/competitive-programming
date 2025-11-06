# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # create a dictionary that hold key: value =>(col): [val1, val2]
        nums = defaultdict(list)
        # iterate over the queue in order to traverse level by level
        queue = deque([(root, 0)])
        row = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node, col = queue.popleft()

                nums[col].append((row, node.val))

                # call the left child 
                if node.left:
                    queue.append((node.left, col-1))

                # call the right child
                if node.right:
                    queue.append((node.right, col+1))

            row += 1

        # sort based on left to right
        nums = sorted(nums.items())
        ans = []
        for _, cols in nums:
            cols = sorted(cols, key=lambda x: (x[0], x[1]))
            vertical = []
            for row, col in cols:
                vertical.append(col)
            ans.append(vertical)

        return ans
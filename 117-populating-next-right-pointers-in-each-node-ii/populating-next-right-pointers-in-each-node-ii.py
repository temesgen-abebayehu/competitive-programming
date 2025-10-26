"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            # Connect all nodes at current level
            for i in range(level_size):
                node = queue.popleft()
                
                # Connect to next node in current level (if not last node)
                if i < level_size - 1:
                    node.next = queue[0]
                else:
                    node.next = None
                
                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root
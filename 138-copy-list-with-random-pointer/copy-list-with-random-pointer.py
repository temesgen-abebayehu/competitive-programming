"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        reference = {}
        node = head
        # First pass: Create a copy of each node and store the mapping. This part is correct.
        while node:
            reference[node] = Node(node.val)
            node = node.next

        # Second pass: Build the new list and set the random pointers correctly.
        dummy = Node(0) # Using 0 for clarity, any value is fine.
        curr = dummy
        node = head # Use a different iterator to not modify the original head
        while node:
            # Get the new node from the reference map
            new_node = reference[node]
            
            # Link it to the new list
            curr.next = new_node
            
            # Set the random pointer for the NEWLY ADDED node
            if node.random:
                new_node.random = reference[node.random]
            
            # Move both pointers forward
            node = node.next
            curr = curr.next

        return dummy.next
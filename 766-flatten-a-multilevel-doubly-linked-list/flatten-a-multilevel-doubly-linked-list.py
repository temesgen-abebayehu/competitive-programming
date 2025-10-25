"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # if head is None
        if not head:
            return head

        # create a variable that hold the head in oreder to maintain head access
        current = head
        
        while current:
            if current.child:
                # Store the next node
                next_node = current.next
                
                # Connect current node to child head
                child_head = self.flatten(current.child)
                current.next = child_head
                child_head.prev = current
                current.child = None
                
                # Find the tail of the child list
                tail = child_head
                while tail.next:
                    tail = tail.next
                
                # Connect child tail to the original next node
                tail.next = next_node
                if next_node:
                    next_node.prev = tail
            
            current = current.next
        
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        l_ptr = less                
        great = ListNode()
        g_ptr = great
        curr = head

        while curr:
            if curr.val < x:
                l_ptr.next = curr
                l_ptr = l_ptr.next
            else:
                g_ptr.next = curr
                g_ptr = g_ptr.next

            curr = curr.next

        g_ptr.next = None        
        l_ptr.next = great.next
        
        return less.next
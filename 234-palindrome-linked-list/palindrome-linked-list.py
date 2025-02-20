# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        pre = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = pre
            pre = curr
            curr = next_node
            
        while pre and temp:
            if pre.val != temp.val:
                return False
            pre = pre.next
            temp = temp.next
        
        return True

        
        
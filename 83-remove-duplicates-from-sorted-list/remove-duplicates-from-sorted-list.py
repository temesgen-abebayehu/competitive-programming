# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0,head)
        pre = dummy.next
        curr = head.next

        while curr:
            if curr.val == pre.val:
                pre.next = curr.next
               
            else:                
                pre = pre.next
            curr = curr.next

        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or (not head.next and n > 0):
            return None
            
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        last = dummy

        count = 0
        while last.next:
            count += 1
            if count > n:
                curr = curr.next
            last = last.next

        if curr.next and curr.next.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ptr = head
        slow = head
        fast = head

        count = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            count += 1
        
        pre = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp

        sums = 0
        while count > 0:
            sums = max(sums, ptr.val + pre.val)
            ptr = ptr.next
            pre = pre.next
            count -= 1
        
        return sums
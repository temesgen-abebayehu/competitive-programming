# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2:
            added1 = added2 = 0
            if l1:
                added1 = l1.val
                l1 = l1.next
            if l2:
                added2 = l2.val
                l2 = l2.next

            sum_digit = added1 + added2 + carry
            
            if sum_digit >= 10:
                carry = 1
                sum_digit = sum_digit - 10
            else:
                carry=0

            curr.next = ListNode(sum_digit)
            curr = curr.next
        if carry > 0:
            curr.next = ListNode(carry)

        return dummy.next
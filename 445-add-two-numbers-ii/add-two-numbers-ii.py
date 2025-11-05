# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. reverse the first list
        curr_l1 = None
        while l1:
            temp = l1.next
            l1.next = curr_l1
            curr_l1 = l1
            l1 = temp
        
        # reverse the second list
        curr_l2 = None
        while l2:
            temp = l2.next
            l2.next = curr_l2
            curr_l2 = l2
            l2 = temp

        # Add the two reversed list
        node = ListNode()
        pre = node
        carry = 0
        while curr_l1 or curr_l2 or carry:
            d1 = 0
            d2 = 0
            if curr_l1:
                d1 = curr_l1.val
                curr_l1 = curr_l1.next

            if curr_l2:
                d2 = curr_l2.val
                curr_l2 = curr_l2.next

            add = d1+d2+carry
            carry = add//10
            add = add % 10

            node.next = ListNode(add)
            node = node.next


        # revese back the added list
        curr_add = None
        node = pre.next
        while node:
            temp = node.next
            node.next = curr_add
            curr_add = node
            node = temp

        return curr_add
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        reverse = None
        slow.next = None
        while second_half:
            temp = second_half.next
            second_half.next = reverse
            reverse = second_half
            second_half = temp

        while head and reverse:
            temp1 = head.next
            temp2 = reverse.next

            # set next node
            head.next = reverse
            reverse.next = temp1

            # call next node
            head = temp1
            reverse = temp2
            
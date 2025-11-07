# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 1. Divide: Split the list into two halves.
        middle = self.get_middle(head)
        right_half = middle.next
        middle.next = None  # Sever the link between the two halves
        left_half = head

        # 2. Conquer: Recursively sort both halves.
        sorted_left = self.sortList(left_half)
        sorted_right = self.sortList(right_half)

        # 3. Combine: Merge the two sorted halves.
        return self.merge(sorted_left, sorted_right)

    def get_middle(self, head):
        """
        Finds the middle node of a linked list using the fast and slow pointer technique.
        """
        if not head:
            return None
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        """
        Merges two sorted linked lists into a single sorted linked list.
        """
        dummy = ListNode()
        tail = dummy

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        # Attach the remaining part of the list
        if left:
            tail.next = left
        elif right:
            tail.next = right

        return dummy.next
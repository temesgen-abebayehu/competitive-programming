# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        res = 0
        start = False
        temp = head

        while temp:
            if temp.val in nums and not start:
                start = True
                res += 1
            elif temp.val not in nums and start:
                start = False
            temp = temp.next

        return res
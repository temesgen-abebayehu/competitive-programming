# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        temp = head
        num = []
        while temp:
            num.append(temp.val)
            temp = temp.next
        
        num.reverse()
        res = 0
        for i in range(len(num)):
            res += 2**i * num[i]

        return res
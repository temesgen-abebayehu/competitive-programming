# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        arr = []
        node  = head

        while node:
            arr.append(node.val)
            node = node.next
        
        idx = bisect_right(arr, x)
        min_arr = []
        max_arr = []
        for e in arr:
            if e < x:
                min_arr.append(e)
            else:
                max_arr.append(e)
        
        dummy = ListNode()
        curr = dummy
        for e in min_arr:
            temp = ListNode(e)
            curr.next = temp
            curr = curr.next
        
        for e in max_arr:
            temp = ListNode(e)
            curr.next = temp
            curr = curr.next

        return dummy.next
        
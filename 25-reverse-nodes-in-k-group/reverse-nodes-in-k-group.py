# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reversed(pre, curr, k):
            pre_head = curr
            for _ in range(k):
                temp = curr.next
                curr.next = pre
                pre = curr
                curr = temp

            return pre, pre_head

        dummy = ListNode()
        dummy.next = head
        pre = dummy
        curr = head        

        while curr:
            ptr = curr
            count = 0
            while ptr and count < k:
                ptr = ptr.next
                count += 1

            if count == k:
                n_head, n_tail = reversed(None, curr, k)
                pre.next = n_head
                n_tail.next = ptr

                pre = n_tail
                curr = ptr
            else:
                break
        return dummy.next
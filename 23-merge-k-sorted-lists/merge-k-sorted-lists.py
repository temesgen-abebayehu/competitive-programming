# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i,lis in enumerate(lists):
            if lis:
                heapq.heappush(min_heap, (lis.val, i, lis))
        
        dummy = ListNode()
        curr = dummy

        while min_heap:
            v, idx, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))
        return dummy.next
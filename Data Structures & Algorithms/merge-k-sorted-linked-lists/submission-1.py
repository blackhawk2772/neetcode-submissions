# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        minHeap = []
        for i, ptr in enumerate(lists):
                if ptr:
                    heapq.heappush(minHeap, (ptr.val, i, ptr))
            
        dummy = ListNode(0)
        curr = dummy

        while minHeap:
            al, i, node = heapq.heappop(minHeap)

            # attach node to result
            curr.next = node
            curr = curr.next

            # push next node from same list
            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))
        
        return dummy.next
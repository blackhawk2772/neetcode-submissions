# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if (n == 1 and not head.next) or not head:
            return None
        
        fast = head
        size = 0
        while fast:
            fast = fast.next
            size += 1

        if n == size:
            nxt = head.next
            head.next = None
            return nxt

        ptr = head

        # size=4; n=2; 
        for i in range(size-n):
            prev = ptr
            ptr = ptr.next
            nxt = ptr.next
        
        if n == 1:
            prev.next = None
        else:
            prev.next = nxt
        
        return head


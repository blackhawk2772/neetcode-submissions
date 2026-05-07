# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        nxt = None

        while head:

            nxt = head.next   # 1. save next
            head.next = prev  # 2. reverse pointer
            prev = head       # 3. move prev
            head = nxt        # 4. move head
            
        return prev
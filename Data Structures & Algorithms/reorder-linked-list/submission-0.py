# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        mid = head
        fast = head.next

        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next
        
        second = mid.next
        prev = mid.next = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        first = head
        second = prev

        while first and second:
            nxt1, nxt2 = first.next, second.next

            first.next = second
            second.next = nxt1
            first = nxt1
            second = nxt2
        
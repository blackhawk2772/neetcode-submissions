# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        output = ListNode()
        co = output
        
        while list1 or list2:

            if list1 and (not list2 or list1.val < list2.val):
                co.next = list1
                co = list1
                list1=list1.next
            elif list2 and (not list1 or list1.val >= list2.val):
                co.next = list2
                co = list2
                list2=list2.next

        return output.next
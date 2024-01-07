# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            # Case 1:if list1 value is smaller than list2, add list1 to current node
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            
            # Case 2:if list2 value is smaller or equal than list1, add list2 to current node
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If there are leftover elements, join them all to current node
        if list1:
            current.next = list1
        if list2:
            current.next = list2
            
        
        return dummy.next
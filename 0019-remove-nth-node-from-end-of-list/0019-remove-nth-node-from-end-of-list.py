# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        trailing, lead = dummy, head
        
        while n > 0:
            lead = lead.next
            n -= 1
            
        while lead:
            trailing = trailing.next
            lead = lead.next
        
        trailing.next = trailing.next.next
        
        return dummy.next
        
        
            
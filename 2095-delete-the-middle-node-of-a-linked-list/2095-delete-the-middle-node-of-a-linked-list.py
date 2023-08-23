# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Find Length
        prevNode = current = head
        n = 0
        while current:
            n += 1
            current = current.next
            
        if n == 1:
            return None
        if n == 2:
            head.next = None
            return head
        
        
        middle = math.floor(n/2) - 1
        
        for i in range(middle):
            prevNode = prevNode.next
        
        temp = prevNode.next.next    
        prevNode.next = temp
        
        return head
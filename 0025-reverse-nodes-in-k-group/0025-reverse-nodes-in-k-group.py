# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        groupPrev = dummy
        
        while True:
            kthNode = self.findKthNode(groupPrev, k)
            if not kthNode:
                break
            
            groupNext = kthNode.next
            prev, current = kthNode.next, groupPrev.next

            while current != groupNext:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            
            temp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = temp
                
        return dummy.next
        
        
        
        
        
    def findKthNode(self, current, k):
        while current and k > 0:
            current = current.next
            k -= 1
        
        return current
        
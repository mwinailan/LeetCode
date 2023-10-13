# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        right = slow
        temp = right.next
        right.next = None
        right = temp
        
        
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
    
    def merge(self, list1, list2):
        
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        
        return dummy.next
        
        
        
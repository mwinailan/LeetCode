# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the middle of the list.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        firstPointer, secondPointer = head, slow.next
        prev = slow.next = None
        
        #Reverse List
        while secondPointer:
            temp = secondPointer.next
            secondPointer.next = prev
            prev = secondPointer
            secondPointer = temp
            
        #prev will be pointing to the head of the second link partition
        while prev:
            temp = firstPointer.next
            firstPointer.next = prev
            temp2 = prev.next
            firstPointer = temp
            prev.next = firstPointer
            prev = temp2
            
            
        
        
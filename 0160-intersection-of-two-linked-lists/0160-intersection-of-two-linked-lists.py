# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def findLength(ln):
            length = 0
            while ln != None:
                ln = ln.next
                length += 1
            return length
        
        difference = abs(findLength(headA) - findLength(headB))
        l1, l2 = headA, headB
        
        def movePointer(ln, difference):
            for i in range(difference):
                ln = ln.next  
            return ln
        
        # Case 1: Move l1 pointer by degree of difference
        if findLength(headA) > findLength(headB):
            l1 = movePointer(l1, difference)
        # Case 2: Move l2 pointer by degree of difference
        elif findLength(headB) > findLength(headA):
            l2 = movePointer(l2, difference)
            
        
        while l1 != l2:
            l1 = l1.next
            l2 = l2.next
        
        return l1
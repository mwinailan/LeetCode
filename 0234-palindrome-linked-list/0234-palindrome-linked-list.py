# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        numArray = []
        curr = head
        
        while curr:
            numArray.append(curr.val)
            curr = curr.next
        
        l, r = 0, len(numArray) - 1
        
        while l < r:
            if numArray[l] != numArray[r]:
                return False
            l += 1
            r -= 1
        
        return True
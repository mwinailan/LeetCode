# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current = root
        k_current = 0
        stack = []
        
        while current or stack:
            # Go traverse to the left element until we cant, append any elements found this way
            while current:
                stack.append(current)
                current = current.left
            # Pop an element from the stack, and increment k_current
            current = stack.pop()
            k_current += 1
            if k_current == k:
                return current.val
            
            # Traverse to the right when we cannot go further left
            current = current.right
        
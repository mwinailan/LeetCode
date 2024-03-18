# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return False
        current = root
        while current:
            # Case 1: both p and q are less than root
            if p.val < current.val and q.val < current.val:
                current = current.left
            # Case 2: both p and q are more than root
            elif p.val > current.val and q.val > current.val:
                current = current.right
            # Case 3: p and q are in different sides of the bst
            else:
                return current
        
        return current
        
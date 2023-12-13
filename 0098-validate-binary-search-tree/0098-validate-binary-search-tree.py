# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS Solution: Check if root is valid using left and right boundaries
        def isValid(node, leftBoundary, rightBoundary):
            if not node:
                return True
            if not (node.val < rightBoundary and node.val > leftBoundary):
                return False
            
            return isValid(node.left, leftBoundary, node.val) and isValid(node.right, node.val, rightBoundary)
        
        return isValid(root, float("-Inf"), float("Inf"))
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def countGoodNodes(node, currentMax):
            if not node:
                return 0
            
            currentMax = max(currentMax, node.val)
            
            if currentMax > node.val:
                return countGoodNodes(node.left, currentMax) + countGoodNodes(node.right, currentMax)
            else:
                return 1 + countGoodNodes(node.left, currentMax) + countGoodNodes(node.right, currentMax)
        
        return countGoodNodes(root, root.val)
        
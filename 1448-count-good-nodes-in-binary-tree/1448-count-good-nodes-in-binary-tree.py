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
                res = 0
            else:
                res = 1
            
            res += countGoodNodes(node.left, currentMax)
            res += countGoodNodes(node.right, currentMax)
            
            return res
        
        
        return countGoodNodes(root, root.val)
        
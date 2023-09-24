# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        
        def findMaxPath(node):
            if not node:
                return 0
            
            maxLeft = max(findMaxPath(node.left), 0)
            maxRight = max(findMaxPath(node.right), 0)
            # no split
            res[0] = max(res[0], node.val + maxLeft + maxRight)
            
            #return split
            return node.val + max(maxLeft, maxRight)
        
        findMaxPath(root)
        return res[0]
        
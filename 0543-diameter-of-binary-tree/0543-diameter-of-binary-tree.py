# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = [0]
        def dfs(root):
            if not root:
                return 0
            right = dfs(root.right)
            left = dfs(root.left)
            maxDiameter[0] = max(maxDiameter[0], right + left)
            return 1 + max(right, left)
        
        dfs(root)
        return maxDiameter[0]
        
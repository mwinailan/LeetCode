# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth = 1
        q = collections.deque()
        q.append([root, 1, 0]) # node, val, level
        prevLevel, levelFirstNum = 0, 1
        
        while q:
            node, val, level = q.popleft()
            if level > prevLevel:
                prevLevel = level
                levelFirstNum = val
            maxWidth = max(maxWidth, val - levelFirstNum + 1)
            
            if node.left:
                q.append([node.left, val * 2, level + 1])
            if node.right:
                q.append([node.right, val * 2 + 1, level + 1])
        return maxWidth
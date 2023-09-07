# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        currentNode = root
        nodeStack = []
        k_current = 0
        
        while currentNode or nodeStack:
            while currentNode:
                nodeStack.append(currentNode)
                currentNode = currentNode.left
            
            currentNode = nodeStack.pop()
            k_current += 1
            
            if (k_current == k):
                return currentNode.val
            currentNode = currentNode.right
        
        
        
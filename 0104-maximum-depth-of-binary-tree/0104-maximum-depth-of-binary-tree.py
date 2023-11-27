# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS Solution
#         if not root:
#             return 0
#         if not root.left and not root.right:
#             return 1
        
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
        
        #Iterative BFS
        nodeQ = collections.deque()
        nodeQ.append(root)
        depthOfTree = 0
        while nodeQ:
            for i in range(len(nodeQ)):
                currNode = nodeQ.popleft()
                if currNode:
                    nodeQ.append(currNode.left)
                    nodeQ.append(currNode.right)
            
            depthOfTree += 1
        
        return depthOfTree - 1
            
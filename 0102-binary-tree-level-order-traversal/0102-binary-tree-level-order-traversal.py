# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelOrderTraversalList = []
        nodeQ = collections.deque()
        nodeQ.append(root)
        
        while nodeQ:
            listAtLevel = []
            sizeCurrent = len(nodeQ)
            for i in range(sizeCurrent):
                currentNode = nodeQ.popleft()
                if currentNode:
                    listAtLevel.append(currentNode.val)
                    nodeQ.append(currentNode.left)
                    nodeQ.append(currentNode.right)
            if listAtLevel:
                levelOrderTraversalList.append(listAtLevel)
        
        return levelOrderTraversalList
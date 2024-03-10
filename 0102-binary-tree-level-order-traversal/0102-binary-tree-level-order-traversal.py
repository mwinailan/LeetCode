# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelOrderRes = []
        q = collections.deque()
        q.append(root)
        
        while q:
            currentLength = len(q)
            currentLevel = []
            for i in range(currentLength):
                curNode = q.popleft()
                if curNode:
                    currentLevel.append(curNode.val)
                    q.append(curNode.left)
                    q.append(curNode.right)
            
            if currentLevel:
                levelOrderRes.append(currentLevel)
        
        return levelOrderRes
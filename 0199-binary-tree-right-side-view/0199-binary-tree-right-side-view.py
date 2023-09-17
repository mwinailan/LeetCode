# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque()
        queue.append(root)
        res = []
        
        while queue:
            levelLen = len(queue)
            currNode = None
            for i in range(levelLen):
                currNode = queue.popleft()
                if currNode:
                    if currNode.left:
                        queue.append(currNode.left)
                    if currNode.right:
                        queue.append(currNode.right)
            
            if currNode:
                res.append(currNode.val)
        
        return res
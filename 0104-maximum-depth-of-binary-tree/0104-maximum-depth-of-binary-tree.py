# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        
        max_depth = 0
        # iterative bfs
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            queue_length = len(queue)
            for _ in range(queue_length):
                current_node = queue.popleft()
                
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            
            max_depth += 1
                
        
        return max_depth
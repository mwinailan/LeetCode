# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if len(nodes) == 1:
            return nodes[0]
        
        selected_nodes = set(nodes)
        # left = parent * 2 + 1
        # right = parent * 2 + 2
        def search_nodes(tree_node):
            # DFS solution
            if tree_node in selected_nodes:
                return tree_node
            if not tree_node:
                return None
            
            left = search_nodes(tree_node.left)
            right = search_nodes(tree_node.right)
            
            if left and right:
                return tree_node
            if left and not right:
                return left
            if right and not left:
                return right
            
            return None
        
        return search_nodes(root)
            
        
        
        
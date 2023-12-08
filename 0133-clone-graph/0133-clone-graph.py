"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew = {}
        # DFS solution to clone
        def clone(node):
            #TODO: Stopping Criteria
            if node in oldToNew:
                return oldToNew[node]
            
            # Make clone node, and run clone recursively on neighbors
            clonedNode = Node(node.val)
            oldToNew[node] = clonedNode
            for neighbor in node.neighbors:
                clonedNode.neighbors.append(clone(neighbor))
            
            return clonedNode
        
        return clone(node)
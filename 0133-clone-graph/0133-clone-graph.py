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
            return
        
        oldToNew = {}
        
        def cloneNodes(node):
            if node in oldToNew:
                return oldToNew[node]
            
            newNode = Node(node.val)
            oldToNew[node] = newNode
            
            for neighbor in node.neighbors:
                oldToNew[node].neighbors.append(cloneNodes(neighbor))
            
            return newNode
    
        
        return cloneNodes(node)
            
            
        
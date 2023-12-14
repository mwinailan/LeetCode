from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        
        # Create adjacency list for edges
        adjList = {i:[] for i in range(n)}
        for e1, e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)

        isVisited = set()
        # DFS solution to mark all nodes
        def markNodes(node, previousNode):
            if node in isVisited:
                return False
            isVisited.add(node)

            for neighbor in adjList[node]:
                if neighbor == previousNode:
                    continue
                if not markNodes(neighbor, node):
                    return False
            return True
        
        return markNodes(0, -1) and n == len(isVisited)

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
        graphMapping = {i: [] for i in range(n)}

        for e1, e2 in edges:
            graphMapping[e1].append(e2)
            graphMapping[e2].append(e1)
        
        isVisited = set()

        def checkNodes(node, prev):
            if node in isVisited:
                return False
            isVisited.add(node)

            for neighbor in graphMapping[node]:
                if neighbor == prev:
                    continue
                else:
                    if not checkNodes(neighbor, node):
                        return False
            return True
        
        return checkNodes(0, -1) and len(isVisited) == n
 

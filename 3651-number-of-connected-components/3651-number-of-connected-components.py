from typing import (
    List,
)

class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        # write your code here
        parent= [i for i in range(n)]
        rank = [1] * n

        def find(n):
            res = n
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return True

        
        connectedGraphs = n
        for s, d in edges:
            if union(s,d):
                connectedGraphs -= 1
        
        return connectedGraphs

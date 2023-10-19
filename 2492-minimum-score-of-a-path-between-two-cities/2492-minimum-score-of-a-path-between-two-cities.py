class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for src, dst, distance in roads:
            adjList[src].append((dst, distance))
            adjList[dst].append((src, distance))
        isVisited = set()
        res = float("inf")
        
        def dfs(i):
            if i in isVisited:
                return
            isVisited.add(i)
            nonlocal res
            for dst, distance in adjList[i]:
                res = min(res, distance)
                dfs(dst)
            
        dfs(1)
        return res
        
        
        
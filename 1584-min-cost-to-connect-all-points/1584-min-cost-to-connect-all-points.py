class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = { i:[] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                edges[i].append([distance, j])
                edges[j].append([distance, i])
        
        isVisited = set()
        frontier = [[0,0]]
        res = 0
        while len(isVisited) < n:
            dist, point = heapq.heappop(frontier)
            if point in isVisited:
                continue
            isVisited.add(point)
            res += dist
            
            for neighborDist, neighbor in edges[point]:
                if neighbor not in isVisited:
                    heapq.heappush(frontier, [neighborDist, neighbor])
        
        return res
                
            
            
        
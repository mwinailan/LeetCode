class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v,w))
        
        isVisited = set()
        totalTime = 0
        
        minHeap = [ (0,k) ]
        heapq.heapify(minHeap)
        
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in isVisited:
                continue
            isVisited.add(n1)
            totalTime = max(totalTime, w1)
            
            for n2, w2 in edges[n1]:
                if n2 in isVisited:
                    continue
                heapq.heappush(minHeap, (w2 + w1, n2))
        
        return totalTime if len(isVisited) == n else -1
        
        
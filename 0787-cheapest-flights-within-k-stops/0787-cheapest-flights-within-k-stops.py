class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        srcToDstDistance = [float("inf")] * n
        srcToDstDistance[src] = 0
        
        for i in range(k+1):
            srcToDstDistanceTemp = srcToDstDistance.copy()
            for s, to, price in flights:
                if srcToDstDistance[s] == float("inf"):
                    continue
                if srcToDstDistance[s] + price < srcToDstDistanceTemp[to]:
                    srcToDstDistanceTemp[to] = srcToDstDistance[s] + price
            srcToDstDistance = srcToDstDistanceTemp
        
        return srcToDstDistance[dst] if srcToDstDistance[dst] != float("inf") else -1
    
            
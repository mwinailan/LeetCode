class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        minHeap = [[grid[0][0],0,0]]
        isVisited = set()
        isVisited.add((0,0))
        
        while minHeap:
            currentHeight, currentRow, currentCol = heapq.heappop(minHeap)
            if currentRow == len(grid) - 1 and currentCol == len(grid) - 1:
                return currentHeight
            for dr, dc in directions:
                newR = currentRow + dr
                newC = currentCol + dc
                if newR not in range(len(grid)) or newC not in range(len(grid)) or (newR, newC) in isVisited:
                    continue
                isVisited.add((newR,newC))
                heapq.heappush(minHeap, [max(currentHeight, grid[newR][newC]), newR, newC])
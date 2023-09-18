# class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:
#         directions = [[0,1], [0,-1], [1,0], [0,1]]
#         minHeap = [[grid[0][0],0,0]]
#         isVisited = set()
#         isVisited.add((0,0))
        
#         while minHeap:
#             currentHeight, currentRow, currentCol = heapq.heappop(minHeap)
#             if currentRow == len(grid) - 1 and currentCol == len(grid) - 1:
#                 return currentHeight
#             for dr, dc in directions:
#                 if (currentRow + dr) < 0 or (currentRow + dr) == len(grid) or (currentCol + dc) < 0 or (currentCol + dc) == len(grid) or (currentRow + dr,currentCol + dc) in isVisited:
#                     continue    
#                 isVisited.add((currentRow + dr, currentRow + dc))
#                 heapq.heappush(minHeap, [max(currentHeight, grid[currentRow + dr][currentCol + dc]), currentRow + dr, currentCol + dc])
                
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]  # (time/max-height, r, c)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (
                    neiR < 0
                    or neiC < 0
                    or neiR == N
                    or neiC == N
                    or (neiR, neiC) in visit
                ):
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])

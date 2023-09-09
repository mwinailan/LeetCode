class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottingOranges = deque()
        freshOranges = 0
        nRows, nCols = len(grid), len(grid[0])
        minMinutes = 0
        for r in range(nRows):
            for c in range(nCols):
                if grid[r][c] == 1:
                    freshOranges += 1
                if grid[r][c] == 2:
                    rottingOranges.append([r,c])
        
        while rottingOranges and freshOranges > 0:
            for i in range(len(rottingOranges)):
                currentRow, currentCol = rottingOranges.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dx, dy in directions:
                    nextRow, nextCol = currentRow + dx, currentCol + dy
                    if nextRow in range(nRows) and nextCol in range(nCols) and grid[nextRow][nextCol] == 1:
                        grid[nextRow][nextCol] = 2
                        rottingOranges.append([nextRow, nextCol])
                        freshOranges -= 1
            minMinutes += 1
        
        if freshOranges == 0:
            return minMinutes
        else:
            return -1
                    
            
        
        
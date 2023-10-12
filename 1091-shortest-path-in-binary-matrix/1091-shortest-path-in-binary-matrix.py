class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        if grid[0][0] == 0:
            q.append((0, 0, 1))
        else:
            return -1
        isVisited = set()
        isVisited.add((0,0))
        
        directions = [[1,0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0,1], [1,1]]
        
        while q:
            currRow, currCol, currLen = q.popleft()
            
            if currRow == (ROWS - 1) and currCol == (COLS - 1):
                return currLen
            
            for dx, dy in directions:
                nextRow = currRow + dx
                nextCol = currCol + dy
                if nextRow in range(ROWS) and nextCol in range(COLS) and (nextRow,nextCol) not in isVisited and grid[nextRow][nextCol] == 0:
                    q.append((nextRow, nextCol, currLen + 1))
                    isVisited.add((nextRow, nextCol))
        
        return -1

        
        
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROW, COLS = len(grid), len(grid[0])
        isVisited = set()

        # DFS solution to mark all islands
        def markIslands(row, col):

                isVisited.add((row,col))
                stack = []
                stack.append([row,col])

                while stack:
                    cRow, cCol = stack.pop()
                    
                    directions = [[1,0],[-1,0],[0,1],[0,-1]]
                    for dx, dy in directions:
                        nRow = cRow + dx
                        nCol = cCol + dy
                        if nRow not in range(ROW) or nCol not in range(COLS) or (nRow,nCol) in isVisited or grid[nRow][nCol] == "0":
                            continue
                        else:
                            stack.append([nRow, nCol])
                            isVisited.add((nRow,nCol))

        numIslands = 0
        # Loop through every grid position and call DFS function        
        for r in range(ROW):
            for c in range(COLS):
                if (r,c) not in isVisited and grid[r][c] == "1":
                    markIslands(r, c)
                    numIslands += 1

        return numIslands

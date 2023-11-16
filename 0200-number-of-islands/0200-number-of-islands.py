class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        isVisited = set()
        
        
        # Use DFS to mark an island starting from coordinates (i, j)
        def markIslands(i, j):
            # TODO: Stopping Criterias
            if i not in range(ROWS) or j not in range(COLS) or (i,j) in isVisited or grid[i][j] == "0":
                return
            
            isVisited.add((i,j))
            
            markIslands(i + 1, j)
            markIslands(i - 1, j)
            markIslands(i, j + 1)
            markIslands(i, j - 1)
        
        numIslands = 0
        # Loop through every point in the grid, and run the DFS function if it meets criterias
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i,j) not in isVisited:
                    markIslands(i, j)
                    numIslands += 1
        
        return numIslands
                    
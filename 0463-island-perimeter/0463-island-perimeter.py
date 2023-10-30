class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # isVisit set value = (i, j)
        isVisited = set()
        
        # DFS solution to find perimeter
        def findPerimeter(i, j):
            #stopping criteria -> i or j is out of bounds, grid[i][j] == 0
            if i not in range(ROWS) or j not in range(COLS) or grid[i][j] == 0:
                return 1
            if (i, j) in isVisited:
                return 0
            
            isVisited.add((i, j))
            #calculate perimeter
            # return perimeter
            return findPerimeter(i + 1, j) + findPerimeter(i - 1, j) + findPerimeter(i, j + 1) + findPerimeter(i, j - 1)
        
        # scan through entire row, and col
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    # go DFS, and return value
                    return findPerimeter(i, j)
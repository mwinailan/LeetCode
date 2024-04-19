class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # isVisit set value = (i, j)
        is_visited = set()
        
        # DFS solution to find perimeter
        def findPerimeter(i, j):
            if i not in range(ROWS) or j not in range(COLS) or grid[i][j] == 0:
                return 1
            if (i,j) in is_visited:
                return 0
            
            is_visited.add((i,j))
            
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            perimeter_length = 0
            for dx, dy in directions:
                perimeter_length += findPerimeter(i + dx, j + dy)

            
            return perimeter_length
            
        # scan through entire row, and col
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    # go DFS, and return value
                    return findPerimeter(i, j)
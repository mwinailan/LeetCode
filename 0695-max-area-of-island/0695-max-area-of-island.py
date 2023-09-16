class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        numRows, numCols = len(grid), len(grid[0])
        isVisited = set()
        
        def findAreaOfIsland(r, c):
            if r not in range(numRows) or c not in range(numCols) or grid[r][c] != 1 or (r,c) in isVisited:
                return 0
            
            isVisited.add((r,c))
            return 1 + findAreaOfIsland(r + 1, c) + findAreaOfIsland(r - 1, c) + findAreaOfIsland(r, c - 1) + findAreaOfIsland(r, c + 1)
        
        maxArea = 0
        for r in range(numRows):
            for c in range(numCols):
                maxArea = max(maxArea, findAreaOfIsland(r,c))
        
        return maxArea
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        isVisited = set()
        numberOfIslands = 0
        
        
        def visitIsland(row, collumn):
            islandQueue = collections.deque()
            isVisited.add((row, collumn))
            islandQueue.append((row, collumn))
            
            while(islandQueue):
                rowCurrent, collumnCurrent = islandQueue.popleft()
                
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for x, y in directions:
                    rowNew = rowCurrent + x
                    collumnNew = collumnCurrent + y
                    
                    if (rowNew in range(len(grid)) and collumnNew in range(len(grid[0])) and grid[rowNew][collumnNew] == "1" and (rowNew, collumnNew) not in isVisited):
                        islandQueue.append((rowNew, collumnNew))
                        isVisited.add((rowNew, collumnNew))
                    
            
        
        for row in range(len(grid)):
            for collumn in range(len(grid[0])):
                if ( grid[row][collumn] == "1" and (row, collumn) not in isVisited):
                    visitIsland(row,collumn)
                    numberOfIslands += 1
        
        return numberOfIslands
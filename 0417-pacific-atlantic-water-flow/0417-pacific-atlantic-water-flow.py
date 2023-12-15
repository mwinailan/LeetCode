class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        flowsToPacific, flowsToAtlantic = set(), set()
        
        # DFS solution to mark (r,c)
        def markLand(r, c, flowsTo, prevHeight):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in flowsTo or heights[r][c] < prevHeight:
                return
            flowsTo.add((r,c))
            
            markLand(r + 1, c, flowsTo, heights[r][c])
            markLand(r - 1, c, flowsTo, heights[r][c])
            markLand(r, c + 1, flowsTo, heights[r][c])
            markLand(r, c - 1, flowsTo, heights[r][c])
            
            
        
        # Iterate through rows
        for r in range(ROWS):
            markLand(r, 0, flowsToPacific, heights[r][0])
            markLand(r, COLS - 1, flowsToAtlantic, heights[r][COLS - 1])
        # Iterate through cols
        for c in range(COLS):
            markLand(0, c, flowsToPacific, heights[0][c])
            markLand(ROWS - 1, c, flowsToAtlantic, heights[ROWS - 1][c])
        
        result = []
        #Iterate through every (r,c) and add to res if both in atlantic and pacific
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in flowsToPacific and (r,c) in flowsToAtlantic:
                    result.append([r,c])
        
        return result
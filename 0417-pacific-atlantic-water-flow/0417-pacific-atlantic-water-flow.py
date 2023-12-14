class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        numOfRows, numOfCols = len(heights), len(heights[0])
        flowsToPacific, flowsToAtlantic = set(), set()
        
        def flowsTo(row, col, oceanName, previousHeight):
            if row not in range(numOfRows) or col not in range(numOfCols) or previousHeight > heights[row][col] or (row,col) in oceanName:
                return
            
            oceanName.add((row, col))
            flowsTo(row + 1, col, oceanName, heights[row][col])
            flowsTo(row - 1, col, oceanName, heights[row][col])
            flowsTo(row, col + 1, oceanName, heights[row][col])
            flowsTo(row, col - 1, oceanName, heights[row][col])
        
        for c in range(numOfCols):
            flowsTo(0, c, flowsToPacific, heights[0][c])
            flowsTo(numOfRows - 1, c, flowsToAtlantic, heights[numOfRows - 1][c])
        
        for r in range(numOfRows):
            flowsTo(r, 0, flowsToPacific, heights[r][0])
            flowsTo(r, numOfCols - 1, flowsToAtlantic, heights[r][numOfCols - 1])
        
        result = []
        for r in range(numOfRows):
            for c in range(numOfCols):
                if (r,c) in flowsToPacific and (r,c) in flowsToAtlantic:
                    result.append([r,c])
        
        return result
        
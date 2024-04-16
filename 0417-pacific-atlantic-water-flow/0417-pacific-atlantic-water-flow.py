class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        flows_to_atlantic = set()
        flows_to_pacific =  set()
        
        # O(n) time, O(n) space complexity
        # DFS Solution
        def mark_grid(r, c, flows_to_ocean, prev_height):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in flows_to_ocean or prev_height > heights[r][c]:
                return
            
            flows_to_ocean.add((r,c))
            
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dx, dy in directions:
                mark_grid(r + dx, c + dy, flows_to_ocean, heights[r][c])
        
        # mark grid starting from the edges
        for r in range(ROWS):
            mark_grid(r, 0, flows_to_pacific, heights[r][0])
            mark_grid(r, COLS - 1, flows_to_atlantic, heights[r][COLS - 1])
            
        for c in range(COLS):
            mark_grid(0, c, flows_to_pacific, heights[0][c])
            mark_grid(ROWS - 1, c, flows_to_atlantic, heights[ROWS - 1][c])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in flows_to_pacific and (r,c) in flows_to_atlantic:
                    res.append([r,c])
        
        return res
                    
                
        
        
        
        
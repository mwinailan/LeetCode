class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [1] * (n)
        
        for _ in range(m - 1):
            top_grid = [1] * (n)
            for i in range(n - 2, -1, -1):
                top_grid[i] = top_grid[i + 1] + grid[i]
            grid = top_grid
        
        return grid[0]
        
            
        
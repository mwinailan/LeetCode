class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        NRows, NCols = len(matrix), len(matrix[0])
        LIP = {} # key= (r,c)
        
        def findLongestPath(r, c, prevValue):
            if r not in range(NRows) or c not in range(NCols) or prevValue >= matrix[r][c]:
                return 0
            if (r,c) in LIP:
                return LIP[(r,c)]
            
            LIP[(r,c)] = 1
            LIP[(r,c)] = max(LIP[(r,c)], 1 + findLongestPath(r + 1, c, matrix[r][c]))
            LIP[(r,c)] = max(LIP[(r,c)], 1 + findLongestPath(r - 1, c, matrix[r][c]))
            LIP[(r,c)] = max(LIP[(r,c)], 1 + findLongestPath(r, c + 1, matrix[r][c]))
            LIP[(r,c)] = max(LIP[(r,c)], 1 + findLongestPath(r, c - 1, matrix[r][c]))
            
            return LIP[(r,c)]
        
        maxIncreasingPath = -1
        for r in range(NRows):
            for c in range(NCols):
                maxIncreasingPath = max(maxIncreasingPath, findLongestPath(r, c, -1))
        
        return maxIncreasingPath
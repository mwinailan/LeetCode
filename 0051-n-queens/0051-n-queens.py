class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        collumnSet = set()
        positiveDiagonalSet = set()
        negativeDiagonalSet = set()
        result = []
        board = [["."] * n for i in range(n)]
        
        def findQueenPositions(r):
            if r == n:
                copy = ["".join(r) for r in board]
                result.append(copy)
                return
            
            for c in range(n):
                if c in collumnSet or (c+r) in positiveDiagonalSet or (r-c) in negativeDiagonalSet:
                    continue
                
                collumnSet.add(c)
                positiveDiagonalSet.add((c+r))
                negativeDiagonalSet.add((r-c))
                board[r][c] = "Q"
                
                findQueenPositions(r + 1)
                
                collumnSet.remove(c)
                positiveDiagonalSet.remove((c+r))
                negativeDiagonalSet.remove((r-c))
                board[r][c] = "."
                
            
        findQueenPositions(0)
        return result
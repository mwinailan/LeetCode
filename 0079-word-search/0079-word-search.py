class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        
        #DFS solution to find words
        def wordExists(r, c, isVisited, i):
            if i == len(word):
                return True
            if r not in range(ROW) or c not in range(COL) or (r,c) in isVisited or board[r][c] != word[i]:
                return False
            
            isVisited.add((r,c))
            res = wordExists(r + 1, c, isVisited, i + 1) or wordExists(r - 1, c, isVisited, i + 1) or wordExists(r, c + 1, isVisited, i + 1) or wordExists(r, c - 1, isVisited, i + 1)
            isVisited.remove((r,c))
            return res
        
        # Iterate through every cell in the grid
        for r in range(ROW):
            for c in range(COL):
                if wordExists(r, c, set(), 0):
                    return True
        
        return False
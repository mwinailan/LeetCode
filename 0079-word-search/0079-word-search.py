class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        isVisitedPath = set()
        
        # DFS appreoach to visit grid tiles
        def findWord(r, c, i):
            #TODO: stopping criteria
            if i == len(word):
                return True
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in isVisitedPath or board[r][c] != word[i]:
                return False
            
            isVisitedPath.add((r,c))
            res = findWord(r + 1, c, i + 1) or findWord(r - 1, c, i + 1) or findWord(r, c + 1, i + 1) or findWord(r, c - 1, i + 1)
            isVisitedPath.remove((r,c))
            
            return res
        
        # Iterate through every tile
        for r in range(ROWS):
            for c in range(COLS):
                if findWord(r, c, 0):
                    return True
        
        return False
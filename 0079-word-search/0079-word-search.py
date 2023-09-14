class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        isVisited = set()
        
        def wordCheck(r, c, index):
            if index == len(word):
                return True
            
            if r not in range(rows) or c not in range(cols) or board[r][c] != word[index] or (r,c) in isVisited:
                return False
            
            isVisited.add((r,c))
            res = wordCheck(r + 1, c, index + 1) or wordCheck(r - 1, c, index + 1) or wordCheck(r, c + 1, index + 1) or wordCheck(r, c - 1, index + 1)
            isVisited.remove((r,c))   
            return res
        
        
        for r in range(rows):
            for c in range(cols):
                if wordCheck(r, c, 0):
                    return True
        
        return False
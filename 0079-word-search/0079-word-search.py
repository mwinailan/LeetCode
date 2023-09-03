class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        isVisited = set()
        
        def findWord(row, col, indexOfWord):
            if indexOfWord == len(word):
                return True
            if row not in range(rows) or col not in range(cols) or board[row][col] != word[indexOfWord] or (row,col) in isVisited:
                return False
            
            isVisited.add((row,col))
            result = findWord(row + 1, col, indexOfWord + 1) or findWord(row - 1, col, indexOfWord + 1) or findWord(row, col + 1, indexOfWord + 1) or findWord(row, col - 1, indexOfWord + 1)
            isVisited.remove((row,col))
            return result
        
        for r in range(rows):
            for c in range(cols):
                if findWord(r, c, 0) == True:
                    return True
        
        return False
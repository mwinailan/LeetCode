class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        topRow = False # Does top row have zero?
        
        # Iterate through every element in matrix and find if we need to set zeroes
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        topRow = True
        
        # Set zeroes for the matrix other than the first collumn and row
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # Set zeroes for the first column
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        # Set zeroes for the first row
        if topRow:
            for c in range(COLS):
                matrix[0][c] = 0
            
                    
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, collumns = len(matrix), len(matrix[0])
        
        top, bottom = 0, rows - 1
        midRow = 0
        while (top <= bottom):
            midRow = (top + bottom) // 2
            if matrix[midRow][-1] < target:
                top = midRow + 1
            elif matrix[midRow][0] > target:
                bottom = midRow - 1
            else:
                break
        
        if not (top <= bottom):
            return False
        
        left, right = 0, collumns - 1
        while (left <= right):
            midCol = (left + right) // 2
            if matrix[midRow][midCol] < target:
                left = midCol + 1
            elif matrix[midRow][midCol] > target:
                right = midCol - 1
            else:
                return True
        
        return False
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1
        while left < right:
            top, bottom = left, right
            for i in range(right - left):
                topLeft = matrix[top][left + i]
                
                # bot left to top left
                matrix[top][left + i] = matrix[bottom - i][left]
                
                # bot right to bot left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                
                # top right to bot right
                matrix[bottom][right - i] = matrix[top + i][right]
                
                # top left to top right
                matrix[top + i][right] = topLeft
            
            left += 1
            right -= 1
        
    
                
                
        
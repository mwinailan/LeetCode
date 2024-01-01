class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1
        while left < right:
            top, bottom = left, right
            for i in range(right - left):
                # Store top left in temp
                temp = matrix[top][left + i]
                
                #element in top left becomes bottom left
                matrix[top][left + i] = matrix[bottom - i][left]
                
                #element in bottom left becomes bottom right
                matrix[bottom - i][left] = matrix[bottom][right - i]
                
                #element in bottom right becomes top right
                matrix[bottom][right - i] = matrix[top + i][right]
                
                #element in top right becomes temp
                matrix[top + i][right] = temp
            
            left += 1
            right -= 1
            
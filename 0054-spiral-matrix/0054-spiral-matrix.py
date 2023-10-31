class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        spiral_order_elements = []
        # Set boundaries
        left, right = 0, COLS
        top, bottom = 0, ROWS
        
        while left < right and top < bottom:
            # Case 1: Traverse all values to the right on the top row boundary
            for i in range(left, right):
                spiral_order_elements.append(matrix[top][i])
            top += 1
            # Case 2: Traverse all values downwards on the right column boundary
            for i in range(top, bottom):
                spiral_order_elements.append(matrix[i][right - 1])
            right -= 1
            
            if not (left < right and top < bottom):
                break
                
            # Case 3: Traverse all values to the left on the bottom row boundary
            for i in range(right - 1, left - 1, -1):
                spiral_order_elements.append(matrix[bottom - 1][i])
            bottom -= 1
            # Case 4: Traverse all values upwards on the left column boundary
            for i in range(bottom - 1, top - 1, -1):
                spiral_order_elements.append(matrix[i][left])
            left += 1
        
        return spiral_order_elements
            
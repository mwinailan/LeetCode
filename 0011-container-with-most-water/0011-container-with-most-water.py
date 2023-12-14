class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        
        # 2 pointer greedy solution
        while (left <= right):
            currentArea = (right - left) * min(height[left], height[right])
            maxArea = max(maxArea, currentArea)
            
            # Case 1: if left height is taller, shift the right pointer
            if height[left] > height[right]:
                right -= 1
            # Case 2: if right height is taller, shift the left pointer
            else:
                left += 1
                
        return maxArea
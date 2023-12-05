class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxWater = 0
        
        
        #2 pointer solution
        while (left < right):
            currentWaterArea = (right - left) * min(height[left], height[right])
            maxWater = max(maxWater, currentWaterArea)
            
            # Case 1: if left height is lower move the left pointer
            if height[left] < height[right]:
                left += 1
            # Case 1: if right height is lower move the right pointer
            else:
                right -= 1
        
        return maxWater
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        rainWater = 0
        
        while left < right:
            if maxLeft <= maxRight:
                left += 1
                if maxLeft - height[left] > 0:
                    rainWater += maxLeft - height[left]
                maxLeft = max(maxLeft, height[left])
                
            else:
                right -= 1
                if maxRight - height[right] > 0:
                    rainWater += maxRight - height[right]
                maxRight = max(maxRight, height[right])
        
        return rainWater
                
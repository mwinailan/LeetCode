class Solution:
    def maxArea(self, height: List[int]) -> int:
        # O(n) time complexity
        maxWaterVolume = 0
        left, right = 0, len(height) - 1
        while(left < right):
            maxWaterVolume = max(maxWaterVolume, (right - left) * min(height[left], height[right]))
            
            #Move the pointers
            # Case 1: left is taller
            if height[left] > height[right]:
                right -= 1
            # Case 2: right is taller
            else:
                left += 1
            
        
        return maxWaterVolume
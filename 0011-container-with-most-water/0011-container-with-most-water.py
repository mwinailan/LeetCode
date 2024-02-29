class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        
        # 2 pointer greedy solution
        while (left <= right):
            currentArea = (right - left) * min(height[right], height[left])
            maxArea = max(maxArea, currentArea)
            
            # Case 1:
            if height[right] > height[left]:
                left += 1
            
            # Case 2:
            else:
                right -= 1
        return maxArea